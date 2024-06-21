# Proyecto de procesado de videos con Python

Este repositorio contiene múltiples scripts en Python diseñados para aplicar efectos de pixelación y ruido estático a imágenes y videos, así como herramientas para manipular y convertir formatos de archivos multimedia. El flujo de trabajo principal incluye la extracción de frames de un video, su pixelación, aplicación de un efecto de ruido, y la reconversión a formato de video.

## Estructura del Proyecto

La estructura del directorio es la siguiente:

- `/examples`: Contiene imágenes y videos de ejemplo.
- `/final_frames`: Almacena los frames finales después de aplicar todos los efectos.
- `/gradient_test`: Directorio de pruebas para gradientes (primera version de la pixelacion).
- `/original_frames`: Contiene los frames extraídos de un video original.
- `/pixelated_frames`: Almacena los frames después de aplicar el efecto de pixelación.
- Scripts:
  - `gui_app.py`: Es la version con interfaz de todas las funcionalidades  
  - `extract_Frames.py`: Extrae frames de un video.
  - `pixelate.py`: Aplica un efecto de pixelación a las imágenes.
  - `pixelate_glitch.py`: Aplica un efecto de pixelación y añade una intermitencia (glitch) a las imágenes cada ciertos frames.
  - `noise_effect_frames.py`: Añade un efecto de ruido estático a las imágenes.
  - `frames_to_mp4.py`: Convierte una secuencia de imágenes en un archivo de video.
  - `rename_files.py`: Renombra archivos en un directorio de forma secuencial.
  - `webcam_live_pixelate.py`: Aplica pixelación en tiempo real a la entrada de una webcam.
  - `youtube_video_downloader.py`: Descarga videos de YouTube.

## Pasos para Ejecutar el Proyecto

Antes que nada hay que descargar el proyecto e instalar dependencias:

``` bash
git clone https://github.com/lexO-dat/pixelated_transform/
```
``` bash
cd pixelated_transform
```
``` bash
pip install -r requeriments.txt
```
## NOTA:
Las imagenes que estan en las carpetas final_frames, original_frames y pixelated_frames los debes borrar, estan solamente para poder subir las carpetas a github.

## Ejecutar con interfaz grafica:

``` bash
python gui_app.py
```

Para transformar un video o imagen este debe estar en la carpeta pixelated_transform (carpeta donde estan todos los scripts), de ser un video solo coloca el nombre, si es una imagen debes agregar la extension de esta.

Se pueden selecciona entre 3 colores:
  - Rojo
  - Verde
  - Azul

El preview solo muestra como quedaria el pixeleo de la imagen, no el noise. Tambien, el slice sirve para poder visualizar distintos frames del video (en caso que sea un video a transformar).

Si se usa el noise recomiendo tener pocas cosas abiertas en el dispositivo, ya que consume bastante CPU (PROXIMAMENTE INTEGRARE TRABAJADO CON GPU)

## NOTA: si quieres usar los scripts por seprado sin interfaz hay espacios comentados dentro de cada uno los cuales dependiendo de lo que busques te permite usarlos.

## Scripts extra:
### Pixelación en Vivo con Webcam
El script `webcam_live_pixelate.py` permite aplicar un efecto de pixelación en tiempo real a la entrada de una webcam. Puedes ajustar el tamaño del bloque, el espacio entre bloques y el factor de brillo antes de ejecutar el script. Asegúrate de que tu webcam esté correctamente conectada y configurada.

Para iniciar la pixelación en vivo:
```bash
python webcam_live_pixelate.py
```

Presiona 'q' para cerrar la ventana de la cámara y terminar la ejecución del script.

### Descarga de Videos de YouTube
El script youtube_video_downloader.py facilita la descarga de videos desde YouTube. Solo necesitas proporcionar el enlace del video de YouTube que deseas descargar. El script descargará la versión de más alta resolución disponible del video.

Para descargar un video de YouTube:
``` bash
python youtube_video_downloader.py
```

Sigue las instrucciones en consola para ingresar la URL del video de YouTube y el script comenzará la descarga automáticamente.

## NOTA:

Antes de ejecutar estos scripts, asegúrate de haber instalado todas las dependencias necesarias:

``` bash
pip install pytube cv2 numpy Pillow

```
