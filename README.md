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
  - `extract_Frames.py`: Extrae frames de un video.
  - `pixelate.py`: Aplica un efecto de pixelación a las imágenes.
  - `noise_effect_frames.py`: Añade un efecto de ruido estático a las imágenes.
  - `frames_to_mp4.py`: Convierte una secuencia de imágenes en un archivo de video.
  - `rename_files.py`: Renombra archivos en un directorio de forma secuencial.
  - `webcam_live_pixelate.py`: Aplica pixelación en tiempo real a la entrada de una webcam.
  - `youtube_video_downloader.py`: Descarga videos de YouTube.

## Librerías Utilizadas

- **Pillow (PIL Fork)**: Manipulación de imágenes.
- **NumPy**: Operaciones numéricas para manipulación de arrays.
- **imageio**: Lectura y escritura de imágenes y videos.
- **OpenCV (cv2)**: Procesamiento de video e imágenes.
- **pytube**: Descarga de videos de YouTube.
- **multiprocessing**: Paralelización de procesos.

## Pasos para Ejecutar el Proyecto

Antes que nada hay que descargar el proyecto e instalar dependencias:

``` bash
git clone https://github.com/lexO-dat/pixelated_transform/
```
``` bash
cd pixelated_transform
```
``` bash
pip install Pillow numpy imageio opencv-python pytube
```

Luego ya se puede empezar a ejecutar los scripts :)

## Pasos para transformar un video

1. **Extracción de Frames**: Utiliza `extract_Frames.py` para extraer frames de un video. Modifica las variables `video_path` y `output_folder` según sea necesario.
   ```bash
   python extract_Frames.py
   ```
2. **Pixelación de Frames**: Utiliza `pixelate.py` para aplicar un efecto de pixelación a los frames extraídos.
    ```bash
   python pixelate.py
   ```
3. **Aplicación de Efecto de Ruido**: Utiliza `noise_effect_frames.py` para añadir ruido estático a los frames pixelados, cabe mencionar que el script utiliza multithreading por lo que recomiendo no tener nada abierto al momento de ejecutarlo.
    ```bash
   python noise_effect_frames.py
   ```
4. **Renombrado de Frames (Opcional)**:los frams deben estar numerados secuencialmente antes de convertirlos en video, si no los tienes asi utiliza `rename_files.py`.
 ```bash
   python rename_files.py
   ```
5. **Conversión de Frames a Video**: `Con frames_to_mp4.py`, convierte los frames procesados de nuevo en un archivo de video.
   ```bash
   python frames_to_mp4.py
   ```

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
