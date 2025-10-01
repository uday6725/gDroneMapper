# === CONFIGURACIÓN INICIAL / USER CONFIGURATION ===

# Ruta del archivo de imagen / Path to the image file
# Puede ser JPG, PNG, DNG / Supported formats: JPG, PNG, DNG
# Puede usarse directorio, "/XXXX/YYYY/xxxx.jpg" / Directories can be used, "/XXXX/YYYY/xxxx.jpg"
jpg_path = "xxxx.jpg"

# ¿El gimbal rota horizontalmente (yaw)? / Does the gimbal rotate horizontally (yaw)?
# Verificar con el manual del drone / Verifiy with drone user manual
# True = Sí / Yes, False = No
gimbal_rotates_yaw = False

# ¿El gimbal rota verticalmente (pitch)? / Does the gimbal rotate vertically (pitch)?
# Verificar con el manual del drone / Verifiy with drone user manual
# True = Sí / Yes, False = No
gimbal_rotates_pitch = True

# Largo de línea de dirección / Heading line length
# Valor numérico / Numeric value
distance_value = 60

# Unidad de longtiud: "m" para metros, "km" para kilómetros / Longitude unit: "m" for meters, "km" for kilometers
distance_unit = "km"

# Punto de referencia manual (opcional) / Manual reference point (optional)
# Coordenadas del objetivo / Target coordinates
# Si no se desea usar objetivo, dejar en None / If not using target, set to None
#
# Números sin comillas / Numbers without quotes
#
# Ejemplo: manual_lat = -34.4711   # Colonia del Sacramento (Uruguay)
# Ejemplo: manual_lon = -57.8440
#
# Ejemplo: manual_lat = None   # Sin punto de referencia / No manual checkpoint
# Ejemplo: manual_lon = None   

manual_lat = None
manual_lon = None

# ¿Usar nombre de archivo personalizado? / Use custom output filename?
# Standard (False): mapa_drone.html
# Custom (True): <IMAGEFILENAME>.html
use_custom_filename = False

# No es neceesario configurar esto / No neeed to configure this setting
# Formato de output / Output format
output_html = "mapa_" + jpg_path.split("/")[-1].split(".")[0] + ".html" if use_custom_filename else "mapa_drone.html"


# FIN de configuración de usuario / END of user configuration

# === IMPORTAR LIBRERÍAS / IMPORT LIBRARIES ===
import subprocess
import json
import math
import folium
import re

def dms_to_decimal(dms_str):
    match = re.match(r"(\d+)\s*deg\s*(\d+)'\s*([\d.]+)\"\s*([NSEW])", dms_str)
    if not match:
        print(f"❌ Formato DMS inválido: {dms_str} / Invalid DMS format")
        exit()
    degrees, minutes, seconds, direction = match.groups()
    decimal = float(degrees) + float(minutes)/60 + float(seconds)/3600
    if direction in ['S', 'W']:
        decimal *= -1
    return decimal

def safe_float(value, name):
    try:
        return float(value)
    except (TypeError, ValueError):
        print(f"❌ Error al convertir '{name}': {value} / Failed to convert '{name}'")
        exit()

def destination_point(lat, lon, bearing_deg, distance_km):
    R = 6371
    bearing_rad = math.radians(bearing_deg)
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    lat2 = math.asin(math.sin(lat_rad) * math.cos(distance_km / R) +
                     math.cos(lat_rad) * math.sin(distance_km / R) * math.cos(bearing_rad))
    lon2 = lon_rad + math.atan2(math.sin(bearing_rad) * math.sin(distance_km / R) * math.cos(lat_rad),
                                math.cos(distance_km / R) - math.sin(lat_rad) * math.sin(lat2))
    return math.degrees(lat2), math.degrees(lon2)

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def bearing_to_target(lat1, lon1, lat2, lon2):
    dlon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(dlon)
    bearing = math.degrees(math.atan2(x, y))
    return (bearing + 360) % 360

def generate_arc_points(lat, lon, start_angle, end_angle, radius_km, steps=30):
    points = []
    angle_step = (end_angle - start_angle) / steps
    for i in range(steps + 1):
        angle = start_angle + i * angle_step
        arc_lat, arc_lon = destination_point(lat, lon, angle, radius_km)
        points.append((arc_lat, arc_lon))
    return points

def get_metadata(jpg_path):
    cmd = ["exiftool", "-j",
           "-GPSLatitude", "-GPSLongitude",
           "-XMP:FlightYawDegree", "-XMP:GimbalYawDegree",
           "-XMP:GimbalPitchDegree", "-XMP:AbsoluteAltitude",
           jpg_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ Error al ejecutar ExifTool / Failed to run ExifTool")
        exit()
    data = json.loads(result.stdout)[0]
    return data

# === EXTRAER METADATOS / EXTRACT METADATA ===
meta = get_metadata(jpg_path)
lat_raw = meta.get("GPSLatitude")
lon_raw = meta.get("GPSLongitude")
lat = dms_to_decimal(lat_raw) if isinstance(lat_raw, str) else safe_float(lat_raw, "GPSLatitude")
lon = dms_to_decimal(lon_raw) if isinstance(lon_raw, str) else safe_float(lon_raw, "GPSLongitude")
flight_yaw = safe_float(meta.get("FlightYawDegree"), "FlightYawDegree")
gimbal_yaw = safe_float(meta.get("GimbalYawDegree"), "GimbalYawDegree") if meta.get("GimbalYawDegree") else None
heading = gimbal_yaw if gimbal_rotates_yaw and gimbal_yaw is not None else flight_yaw
distance_km = distance_value / 1000 if distance_unit == "m" else distance_value
dest_lat, dest_lon = destination_point(lat, lon, heading, distance_km)

# === ZOOM ADAPTATIVO / ADAPTIVE ZOOM ===
zoom_start = 13 if distance_km < 5 else 10

# === CREAR MAPA / CREATE MAP ===
m = folium.Map(location=[lat, lon], zoom_start=zoom_start)
folium.TileLayer('OpenStreetMap', name='Calles / Streets').add_to(m)
folium.TileLayer('CartoDB positron', name='Claro / Light').add_to(m)
folium.TileLayer('CartoDB dark_matter', name='Oscuro / Dark').add_to(m)
folium.TileLayer(
    tiles='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
    name='Satélite alternativo / Alt Satellite',
    attr='Tiles © OpenStreetMap contributors'
).add_to(m)
folium.LayerControl().add_to(m)

# === MARCADORES Y LÍNEAS / MARKERS AND LINES ===
folium.Marker([lat, lon], popup="Drone").add_to(m)
folium.PolyLine([[lat, lon], [dest_lat, dest_lon]], color="red", weight=3,
                tooltip=f"Dirección / Heading {heading:.2f}°").add_to(m)

if manual_lat is not None and manual_lon is not None:
    folium.Marker([manual_lat, manual_lon], popup="Objetivo / Target",
                  icon=folium.Icon(color="blue")).add_to(m)
    folium.PolyLine([[lat, lon], [manual_lat, manual_lon]], color="blue", weight=2,
                    tooltip="Dirección al objetivo / Target direction").add_to(m)

    target_bearing = bearing_to_target(lat, lon, manual_lat, manual_lon)
    angle_diff = abs(heading - target_bearing)
    angle_diff = min(angle_diff, 360 - angle_diff)
    distance_to_target = haversine_distance(lat, lon, manual_lat, manual_lon)

    arc_points = generate_arc_points(lat, lon, heading, target_bearing, radius_km=0.5)
    folium.PolyLine(arc_points, color="purple", weight=2,
                    tooltip="Ángulo visual entre rumbo y objetivo / Visual angle").add_to(m)

    folium.Marker([(lat + manual_lat)/2, (lon + manual_lon)/2],
        popup=f"📐 Ángulo: {angle_diff:.2f}°\n📏 Distancia: {distance_to_target:.2f} km",
        icon=folium.DivIcon(html=f"<div style='font-size:12px;color:#003;'>↔ {angle_diff:.1f}° / {distance_to_target:.2f} km</div>")
    ).add_to(m)

# === EXPORTAR MAPA / EXPORT MAP ===
try:
    m.save(output_html)
    print(f"✅ Mapa generado correctamente: {output_html} / Map successfully generated: {output_html}")
except Exception as e:
    print(f"❌ Error al guardar el mapa / Failed to save map: {e}")

