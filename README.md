🇦🇷 Mapa de Dirección del Drone (opcional con punto manual de referencia) 100% open source, escrito en Python

¿Qué hace?

📍 Extrae la ubicación y orientación del drone desde una imagen aérea (JPG, PNG o DNG) usando ExifTool 📏 Dibuja una línea de dirección desde el drone hacia donde apunta, con longitud configurable 🎯 Opcionalmente compara con un objetivo manual (como Colonia del Sacramento) y calcula distancia y ángulo 🗺️ Genera un mapa interactivo HTML con capas globales (calles, claro, oscuro, satélite alternativa) 🌀 Archivo de salida de nombre configurable

Testeado con DJI Air 3S, debería ser compatible con todos los DJI y otras marcas que utilicen el perfil estarandizado XPM en las imágenes.

🖥️ ¿Qué necesito?

El archivo con el código (gdrone_direction_mapper.py)
Python (https://www.python.org/downloads)
Folium para Phyton (línea de comandos en Windows, ejecutar: "pip install folium")
ExifTool (https://exiftool.org/), únicamente el que dice Windows 64-bit, colocar en el mismo directorio que colocaremos el archivo del código (ver debajo), renombrando exiftool(-K).exe a exiftool.exe
⚠️ ¿Qué elementos son de configuración OBLIGATORIA?

jpg_path: ruta del archivo de imagen con metadatos GPS
distance_value: número, longitud de la línea en metros o kilómetros
distance_unit: "m" o "km" según la unidad elegida, metros o kilómetros
🧩 Parámetros opcionales / Optional user options

manual_lat y manual_lon: coordenadas del objetivo manual (usar None si no se desea)
gimbal_rotates_yaw: si el gimbal controla el giro horizontal (True o False)
gimbal_rotates_pitch: si el gimbal controla el ángulo vertical (True o False)
use_custom_filename: si se desea que el archivo HTML se nombre automáticamente según la imagen (True o False)
👨‍💻 Código

Copiar y pegar en un block de notas
Recordá editar "drone_view.py" para ajustarlo a tus preferencias e indicar el nombre de la fotografía a evaluar.
Guardar como "drone_view.py" o como prefieras
Colocá las imágenes en el mismo directorio que "drone_view.py"
Ejectuar "python drone_view.py" desde la línea de comandos o doble click desde el Explorador
El código responderá con el resultado.
🇺🇸 Drone Heading Mapper (with optional reference point) 100% open source, written in Python

What does it do? 📍 Extracts drone location and heading from aerial image metadata 📏 Draws a heading line from the drone with customizable length 🎯 Optionally compares with a manual target and calculates distance and angle 🗺️ Generates an interactive HTML map with global layers 🌀 Custom file name output

Tested with a DJI Air 3S, it should be compatible with all DJI models and other brands that use standarized XPM profiles in their images.

🖥️ What do I need?

File with the code (gdrone_direction_mapper.py)
Python: https://www.python.org/downloads
Folium in Python (Windows command line: run pip install folium)
ExifTool: https://exiftool.org — choose Windows 64-bit only, place it in the same folder where you'll save the code file (see below), and rename exiftool(-K).exe to exiftool.exe
⚠️ What are the MANDATORY configuration parameters?

jpg_path: Path to the image file with GPS metadata
distance_value: Number, line length in meters or kilometers
distance_unit: "m" or "km", line length in meters or kilometers
🧩 Parámetros opcionales / Optional user options

manual_lat y manual_lon: Manual target coordinates (use None to disable)
gimbal_rotates_yaw: Whether the gimbal controls horizontal yaw (True o False)
gimbal_rotates_pitch: Whether the gimbal controls vertical pitch (True o False)
use_custom_filename: Whether to auto-name the HTML file based on the image (True o False)
👨‍💻 Code

Copy and paste the code into a plain text editor
Edit "drone_view.py" to adjust preferences and specify the name of the photo to analyze
Save it as "drone_view.py" or any name you prefer
Place the image(s) in the same folder as "drone_view.py"
Run "python drone_view.py" from the command line or double-click it from File Explorer
The code will respond with the result
