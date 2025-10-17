****************
(1) 🇦🇷 Español<br>
(2) 🇺🇸 English
****************

## 🇦🇷 (1) Mapeador Fotográfico para Drones<br>
Version 0.3

> Adelanto versión 1.0 Gamma (17/oct): https://gershu-ar.github.io/gDroneMapper/Peek%20-%20gDroneMapper_1_0_Gamma.jpg<br>
> Estoy trabajando para lanzar todo en estos días en forma; no quiero "apurar" el asado :D<br>
> Live preview del mapa, nueva versión: https://gershu-ar.github.io/gDroneMapper

### ¿Qué hace?<br>
📍 Extrae la ubicación y orientación del drone desde una imagen aérea (JPG, PNG o DNG) usando ExifTool<br>
📏 Dibuja una línea de dirección desde el drone hacia donde apunta, con longitud configurable<br>
🎯 Opcionalmente compara con un objetivo manual y calcula distancia y ángulo<br>
🗺️ Genera un mapa interactivo HTML con capas globales (calles, claro, oscuro, satélite alternativa)<br>
🌀 Archivo de salida con nombre estandar o personalizado

Ejemplo en vivo: https://gershu.ar/playground/gdrone_direction_mapper03.html<br>
Muestra: DNG (DJI Air 3S).  Punto de referencia manual (línea azul): Plaza de Mayo, Buenos Aires, Argentina.  Línea roja: dirección del drone al momento de capturar la fotografía.

> Esta versión procesa un archivo por vez.

> Testeado con JPGs y DNGs capturados por un DJI Air 3S, debería ser compatible con todos los DJI y otras marcas que utilicen el perfil estarandizado XPM en las imágenes.

### 🖥️ ¿Qué necesito?
- El archivo con el código (gdrone_direction_mapperXX.py)
- Python (https://www.python.org/downloads) + Folium para Phyton (línea de comandos en Windows, ejecutar: "pip install folium")
- Descargar ExifTool (https://exiftool.org/), el que dice Windows 32 o 64-bit -o el SO que estés usando, debería de funcionar en todos)
- Descomprimir "exiftool(-k).exe" y el directorio "/exiftool_files"/ en el mismo directorio que colocaremos "gdrone_direction_mapperXX.py" y las imágenes a evaluar.
- Renombrar "exiftool(-K).exe" a "exiftool.exe"

 > El XX en "gdrone_direction_mapperXX.py" corresponde a la última versión disponible.  Las versiones anteriores se van eliminando.

### ⚠️ ¿Qué elementos son de configuración OBLIGATORIA?
- jpg_path: ruta del archivo de imagen con metadatos GPS
- distance_value: número, longitud de la línea en metros o kilómetros
- distance_unit: "m" o "km" según la unidad elegida, metros o kilómetros

### 🧩 Parámetros opcionales / Optional user options
- manual_lat y manual_lon: coordenadas del objetivo manual (usar None si no se desea)
- gimbal_rotates_yaw: si el gimbal controla el giro horizontal (True o False)
- gimbal_rotates_pitch: si el gimbal controla el ángulo vertical (True o False)
- use_custom_filename: si se desea que el archivo HTML se nombre automáticamente según la imagen (True o False)

### 👨‍💻 Código
- Descargá gdrone_direction_mapperXX.py
- Recordá editar "gdrone_direction_mapperXX.py" para ajustarlo a tus preferencias e indicar el nombre de la fotografía a evaluar.
- Colocá las imágenes en el mismo directorio que "gdrone_direction_mapperXX.py" y el ExifTool.exe y el directorio "/exiftool_files"/ 
- Ejectuar "python gdrone_direction_mapperXX.py" desde la línea de comandos o doble click desde el Explorador de Windows
- El código responderá con el resultado.

> De encontrar errores, avisar, por favor.<br><br>

**Futuras versiones inclurán mejoras, algunas planeadas:**

- Chequeo previo de software instalado
- Procesamiento por lotes de varios archivos a la vez por directorio
- Gráfica adicional informativa sobre el mapa HTML
- Puntos de referencia adicionales
- Mapa con los puntos de referencia adicionales unificados en formato HTML dinámico o imagen estática
- Proceso de ejecución simplificado
- Formato de salida múltiple: mapa HTML dinámico y/o mapa en imagen estática en directorio y nombre de archivo personalizables
- Herramienta ExifTool ya embebida o incorporada


Coded con ❤️ en 🇦🇷 Argentina

----

## 🇺🇸 (2) Drone Photography Mapper<br>
Version 0.3

> Peek at 1.0 Gamma version (17/oct): https://gershu-ar.github.io/gDroneMapper/Peek%20-%20gDroneMapper_1_0_Gamma.jpg<br>
> I'm working on the frontend and installation, don't want to rush the BBQ! :D<br>
> New version, live map preview: https://gershu-ar.github.io/gDroneMapper

### What does it do?<br>
📍 Extracts drone location and heading from aerial image metadata<br>
📏 Draws a heading line from the drone with customizable length<br>
🎯 Optionally compares with a manual target and calculates distance and angle<br>
🗺️ Generates an interactive HTML map with global layers<br>
🌀 Standard or custom file name output

Live example: https://gershu.ar/playground/gdrone_direction_mapper03.html<br>
Sample: DNG (DJI Air 3S).  Manual checkpoint (blue line): Plaza de Mayo, Buenos Aires, Argentina.  Red line: heading the drone was on the moment it took the picture.

> This version processes one file at a time.

> Tested with JPGs and DNGs captured by a DJI Air 3S, it should be compatible with all DJI models and other brands that use standarized XPM profiles in their images.

### 🖥️ What do I need?
- File with the code (gdrone_direction_mapperXX.py)
- Python (https://www.python.org/downloads)
- Folium in Python (Run Windows command line: "pip install folium")
- ExifTool: https://exiftool.org — Windows 32 or 64-bit -or any OS you're using, it should work everywhere-
- Decompress "exiftool(-K).exe" and "/exiftool_files"/ to the same folder where you saved "gdrone_direction_mapperXX.py" and pictures will be placed for evaluation.
- Rename "exiftool(-K).exe" to "exiftool.exe"

> The XX in "gdrone_direction_mapperXX.py" corresponds to the latest available version for downloading.  Older versions are deleted.

### ⚠️ What are the MANDATORY configuration parameters?
- jpg_path: Path to the image file with GPS metadata
- distance_value: Number, line length in meters or kilometers
- distance_unit: "m" or "km", line length in meters or kilometers

### 🧩 Parámetros opcionales / Optional user options
- manual_lat y manual_lon: Manual target coordinates (use None to disable)
- gimbal_rotates_yaw: Whether the gimbal controls horizontal yaw (True o False)
- gimbal_rotates_pitch: Whether the gimbal controls vertical pitch (True o False)
- use_custom_filename: Whether to auto-name the HTML file based on the image (True o False)

### 👨‍💻 Code
- Download gdrone_direction_mapper.py
- Edit "gdrone_direction_mapperXX.py" to adjust preferences and specify the name of the photo to analyze
- Place the image(s) in the same folder as "gdrone_direction_mapperXX.py", ExifTool.exe and "/exiftool_files"/ directory
- Run "python "gdrone_direction_mapperXX.py" from the command line or double-click it from Windows File Explorer
- The code will respond with the result

> If you find a bug, please, let me know.<br><br>

**Future versions will improve the process, some in consideration are:**

- Software requirements check-up
- Input file batch processing by directory
- Extra informative overlays on HTML the map
- Extra waypoints to add
- Multiple concatenated waypoints view on single HTML mal and/or static map image
- Simplify the script execution process
- Multiple output: HTML map and/or static map image in custom or pre-set directory with custom or pre-set file names
- ExifTool embedded or incorporated

Coded with ❤️ in 🇦🇷 Argentina
