import flet as ft
import os
import pixelate
import pixelate_glitch
import noise_effect_frames
import frames_to_mp4
import extract_Frames
import tempfile
import clean_directory

def main(page: ft.Page):
    page.title = "Procesador de imagenes y videos"

    #Controles
    #Radio buttons para seleccionar si se procesará un video o una imagen
    media_type = ft.RadioGroup(
        value="video",
        content=ft.Row(
            [
                ft.Radio(value="video", label="Video"),
                ft.Radio(value="image", label="Imagen"),
            ]
        ),
    )

    color = ft.RadioGroup(
        value="blue",
        content=ft.Row([
            ft.Radio(value="red", label="Rojo"),
            ft.Radio(value="blue", label="Azul"),
            ft.Radio(value="green", label="Verde"),
        ])
    )

    #Campo de texto para ingresar el nombre del video o imagen
    video_entry = ft.TextField(label="Nombre del video o imagen:", width=300)
    info_video_label = ft.Text(value="", size=14, color=ft.colors.INDIGO_100)
    def show_video_info(e):
        info_video_label.value = "video sin extension, si es imagen agregar extension (ejemplo: imagen.jpg)"
        page.update()
    def hide_video_info(e):
        info_video_label.value = ""
        page.update()
    video_entry.on_focus = show_video_info
    video_entry.on_blur = hide_video_info

    #Checkbox para aplicar glitch
    glitch_var = ft.Checkbox(label="Apply Glitch")

    #Campos de texto para ingresar los valores de los parametros del glitch
    glitch_frame_entry = ft.TextField(label="Glitch frame interval:", disabled=True)
    info_glitch_label = ft.Text(value="", size=14, color=ft.colors.INDIGO_100)
    def show_glitch_info(e):
        info_glitch_label.value = "Mientras más grande el numero menos se verá el glitch."
        page.update()
    def hide_glitch_info(e):
        info_glitch_label.value = ""
        page.update()
    glitch_frame_entry.on_focus = show_glitch_info
    glitch_frame_entry.on_blur = hide_glitch_info

    #Campos de texto para ingresar los valores de los parametros del tamaño del bloque, espacio entre bloques y brillo
    #--------------------------------------------------------------------------------
    block_size_entry = ft.TextField(label="Tamaño del bloque:")
    info_size_label = ft.Text(value="", size=14, color=ft.colors.INDIGO_100)
    def show_size_info(e):
        info_size_label.value = "Que tantos pixeles abarca 1 bloque."
        page.update()
    def hide_size_info(e):
        info_size_label.value = ""
        page.update()
    block_size_entry.on_focus = show_size_info
    block_size_entry.on_blur = hide_size_info

    spacing_entry = ft.TextField(label="Espacio entre bloque:")
    info_space_label = ft.Text(value="", size=14, color=ft.colors.INDIGO_100)
    def show_space_info(e):
        info_space_label.value = "Que tantos pixeles abarca un espacio, recomiendo el mismo valor que el tamaño del bloque."
        page.update()
    def hide_space_info(e):
        info_space_label.value = ""
        page.update()
    spacing_entry.on_focus = show_space_info
    spacing_entry.on_blur = hide_space_info

    brightness_entry = ft.TextField(label="Brightness:")
    info_brightness_entry_label = ft.Text(value="", size=14, color=ft.colors.INDIGO_100)
    def show_brightness_entry_info(e):
        info_brightness_entry_label.value = "Valor de brillo, 1 es el brillo normal y de aplicar recomiendo 1.1 a 1.7"
        page.update()
    def hide_brightness_entry_info(e):
        info_brightness_entry_label.value = ""
        page.update()
    brightness_entry.on_focus = show_brightness_entry_info
    brightness_entry.on_blur = hide_brightness_entry_info

    #--------------------------------------------------------------------------------

    #Checkbox para aplicar ruido (granulado de pelicula)
    noise_var = ft.Checkbox(label="Apply Noise")
    noise_intensity_entry = ft.TextField(label="Noise intensity:", disabled=True)
    info_noise_intensity_label = ft.Text(value="", size=14, color=ft.colors.INDIGO_100)
    def show_noise_intensity_info(e):
        info_noise_intensity_label.value = "Recomiendo valores de 0.1 a 0.5."
        page.update()
    def hide_noise_intensity_info(e):
        info_noise_intensity_label.value = ""
        page.update()
    noise_intensity_entry.on_focus = show_noise_intensity_info
    noise_intensity_entry.on_blur = hide_noise_intensity_info

    #Slider para seleccion de frame
    slide_text = ft.Text("Selecciona frame a previsualizar:", disabled=False)
    frame_text = ft.Text("", disabled=False)
    frame_number = ft.Slider(min=1, max=30, divisions=30, value=1, label="{value}", disabled=False)

    #Boton para procesar el video
    process_button = ft.TextButton(text="Procesar archivo")

    #Texto para mostrar que el video ha sido procesado 
    terminado = ft.Text(value="", size=20, color=ft.colors.GREEN)

    #Imagen para mostrar la vista previa
    preview_image = ft.Image(width=400, height=400)
    #Boton para mostrar la vista previa
    preview_button = ft.TextButton(text="Vista Previa")

    #Texto para mostrar errores (en caso de campos, path, etc)
    error_message = ft.Text(value="", size=15, color=ft.colors.RED)

    #eventos de los controles (que pasa cuando se marcan los checkbox, se presiona el boton, etc)
    glitch_var.on_change = lambda e: toggle_glitch(e, glitch_frame_entry)
    noise_var.on_change = lambda e: toggle_noise(e, noise_intensity_entry)
    process_button.on_click = lambda e: process_video(e, video_entry, glitch_var, noise_var, block_size_entry, spacing_entry, brightness_entry,  glitch_frame_entry, 
                                                      noise_intensity_entry, page, terminado, media_type, error_message, color)
    
    preview_button.on_click = lambda e: preview_frame(e, video_entry, glitch_var, noise_var, block_size_entry, spacing_entry, brightness_entry, glitch_frame_entry, 
                                                      noise_intensity_entry, page, preview_image, error_message, media_type, frame_number, frame_text, slide_text, color)

    #Fila con los controles de video y tipo de media
    row = ft.Row(
        controls=[video_entry, media_type],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True
    )

    row2 = ft.Row(
        controls=[color],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True
    )
    
    #Ordenamiento general en columnas
    #----------------------------------------------------------------------------------------
    left_column = ft.Column(
        controls=[
            row, info_video_label, glitch_var, glitch_frame_entry, info_glitch_label,
            block_size_entry, info_size_label, spacing_entry, info_space_label,
            brightness_entry, info_brightness_entry_label, noise_var, noise_intensity_entry,
            info_noise_intensity_label, process_button
        ],
        alignment=ft.MainAxisAlignment.START,
        width=500
    )

    center_column = ft.Column(
        controls=[],
        width=150
    )

    right_column = ft.Column(
        controls=[row2, preview_image, slide_text, frame_text, frame_number , preview_button, error_message, terminado],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True
    )

    main_row = ft.Row(
        controls=[left_column, center_column, right_column],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
        height=1000
    )
    #----------------------------------------------------------------------------------------

    #Añadir controles a la página
    page.add(main_row)
    page.update()

def disable_silder(e, frame_number, frame_text, slide_text):
    frame_number.disabled = not e.control.value
    frame_text.disabled = not e.control.value
    slide_text.disabled = not e.control.value
    e.page.update()

#Funciones de los eventos
#funcion para deshabilitar y/o habilitar el campo de texto de glitch
def toggle_glitch(e, glitch_frame_entry):
    glitch_frame_entry.disabled = not e.control.value
    e.page.update()

#funcion para deshabilitar y/o habilitar el campo de texto de noise
def toggle_noise(e, noise_intensity_entry):
    noise_intensity_entry.disabled = not e.control.value
    e.page.update()

#funcion para mostrar la vista previa de la imagen (usa pixelate pero solo se extrae el frame 1 del video o imagen)
def preview_frame(e, video_entry, glitch_var, noise_var, block_size_entry, spacing_entry, brightness_entry, glitch_frame_entry, noise_intensity_entry, page, preview_image, error_message, media_type, frame_number, frame_text, slide_text, color):
    try:
        #Si hay bloques que no estan rellenados se muestra un mensaje de error (en este caso los de tamaño de bloque, espacio entre bloques y brillo)
        if not block_size_entry.value or not spacing_entry.value or not brightness_entry.value:
            error_message.value = "Por favor, rellena todos los campos: Tamaño del bloque, Espacio entre bloque y Brillo."
            page.update()
            return
        #si es un video el que se procesará se le hara el proceso de extraer el frame 1, pixelate y noise effect (en caso que aplique)
        if media_type.value == "video":
            video = f'{video_entry.value}.mp4'
            glitch = glitch_var.value

            base_path = os.path.dirname(os.path.abspath(__file__))
            original_frames_path = os.path.join(base_path, 'original_frames')

            #se setean los valores maximos de frames del slide a la cantidad de frames que tenga el video
            frame_text.value = f"selecciona un frame de 1 a {extract_Frames.ct_frames(os.path.join(base_path, video))}"
            slide_text.value = "Selecciona frame:"
            frame_number.disabled = False
            frame_number.max = extract_Frames.ct_frames(os.path.join(base_path, video))
            frame_number.divisions = frame_number.max

            #Se extrae el frame deseado y se pixela
            extract_Frames.extract_frame(os.path.join(base_path, video), original_frames_path, int(frame_number.value))

            first_frame_path = os.path.join(original_frames_path, 'preview.png')

            #Se crea un archivo temporal para mostrar la vista previa
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                preview_path = tmp.name

            #Se aplica el pixelate con o sin glitch
            if glitch:
                pixelate_glitch.pixelate_glitch(first_frame_path, preview_path, int(block_size_entry.value), int(spacing_entry.value), float(brightness_entry.value), 1, int(glitch_frame_entry.value), color.value)
            else:
                pixelate.pixelate(first_frame_path, preview_path, int(block_size_entry.value), int(spacing_entry.value), float(brightness_entry.value), color.value)

            preview_image.src = preview_path
            page.update()
        else:
            image = f'{video_entry.value}'

            glitch = glitch_var.value

            base_path = os.path.dirname(os.path.abspath(__file__))
            original_frames_path = os.path.join(base_path, 'original_frames')

            #se setean los valores maximos de frames del slide a la cantidad de frames que tenga el video
            frame_text.value = ""
            slide_text.value = ""
            frame_number.disabled = True

            #se hace una copia de la imagen
            extract_Frames.copy_image_with_new_name(os.path.join(base_path, image), os.path.join(original_frames_path, 'preview.png'))

            first_frame_path = os.path.join(original_frames_path, 'preview.png')

            #Se crea un archivo temporal para mostrar la vista previa
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                preview_path = tmp.name

            #Se aplica el pixelate con o sin glitch
            if glitch:
                pixelate_glitch.pixelate_glitch(first_frame_path, preview_path, int(block_size_entry.value), int(spacing_entry.value), float(brightness_entry.value), 1, int(glitch_frame_entry.value), color.value)
            else:
                pixelate.pixelate(first_frame_path, preview_path, int(block_size_entry.value), int(spacing_entry.value), float(brightness_entry.value), color.value)

            preview_image.src = preview_path
            page.update()
    except Exception as err:
        error_message.value = f"Error: {err}"
        page.update()


def process_video(e, video_entry, glitch_var, noise_var, block_size_entry, spacing_entry, brightness_entry, glitch_frame_entry, noise_intensity_entry, page, terminado, media_type, error_message, color):
    try:
        if media_type.value == "video":
            video = f'{video_entry.value}.mp4'
            glitch = glitch_var.value
            noise = noise_var.value

            base_path = os.path.dirname(os.path.abspath(__file__))
            original_frames_path = os.path.join(base_path, 'original_frames')
            pixelated_frames_path = os.path.join(base_path, 'pixelated_frames')
            final_frames_path = os.path.join(base_path, 'final_frames')

            terminado.value = "Procesando video, espera un momento..."
            page.update()
            print("Procesamiento de video iniciado.")
            terminado.value = "Extrayendo frames..."
            page.update()
            count = extract_Frames.ct_frames(os.path.join(base_path, video))
            extract_Frames.extract_frames(os.path.join(base_path, video), original_frames_path, terminado)

            if glitch:
                for i in range(1, count):
                    pixelate_glitch.pixelate_glitch(os.path.join(original_frames_path, f'{i}.png'), os.path.join(pixelated_frames_path, f'{i}.png'), int(block_size_entry.value), int(spacing_entry.value), float(brightness_entry.value), i - 1, int(glitch_frame_entry.value), color.value)
                    terminado.value = f'Frame {i} pixeleado con glitch.'
                    page.update()
                    print(f'Frame {i} pixelated with glitch.')
                terminado.value = f'Frame {i} pixeleado.'
                clean_directory.clean_up_directory(original_frames_path)
            else:
                for i in range(1, count):
                    pixelate.pixelate(os.path.join(original_frames_path, f'{i}.png'), os.path.join(pixelated_frames_path, f'{i}.png'), int(block_size_entry.value), int(spacing_entry.value), float(brightness_entry.value), color.value)
                    terminado.value = f'Frame {i} pixeleado.'
                    page.update()
                    print(f'Frame {i} pixelated')
                terminado.value = f'Frame {i} pixeleado.'
                clean_directory.clean_up_directory(original_frames_path)

            if noise:
                terminado.value = "pixeleo con ruido en proceso..."
                page.update()
                noise_effect_frames.process_folder(pixelated_frames_path, final_frames_path, float(noise_intensity_entry.value))
                terminado.value = "pixeleo con ruido terminado, creando video..."
                page.update()
                clean_directory.clean_up_directory(pixelated_frames_path)
                frames_to_mp4.create_video_from_frames(final_frames_path, base_path, 'output.mp4')
                clean_directory.clean_up_directory(final_frames_path)
            else:
                frames_to_mp4.create_video_from_frames(pixelated_frames_path, base_path, 'output.mp4')
                clean_directory.clean_up_directory(pixelated_frames_path)

            print("Procesamiento de video terminado.")
            terminado.value = "Procesamiento de video terminado, puedes ver el video en la misma carpeta de este script."
            page.update()
        else:
            image = f'{video_entry.value}'
            glitch = glitch_var.value
            noise = noise_var.value

            base_path = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(base_path, image)
            pixelated_frames_path = os.path.join(base_path, 'pixelated_frames')
            final_frames_path = os.path.join(base_path, 'final_frames')

            terminado.value = "Procesando imagen, espera un momento..."
            page.update()
            print("Procesamiento de imagen iniciado.")

            if glitch:
                pixelate_glitch.pixelate_glitch(image_path, os.path.join(base_path, 'out.png'), int(block_size_entry.value), int(spacing_entry.value), float(brightness_entry.value), 1, int(glitch_frame_entry.value), color.value)
                terminado.value = "pixeleo con glitch terminado."
                page.update()
                print(f'Imagen pixeleada con glitch.')
            else:
                pixelate.pixelate(image_path, os.path.join(base_path, 'out.png'), int(block_size_entry.value), int(spacing_entry.value), float(brightness_entry.value), color.value)
                terminado.value = "pixeleo terminado."
                page.update()
                print(f'Imagen pixeleada.')

            if noise:
                noise_effect_frames.apply_static_noise(os.path.join(base_path, 'out.png'), os.path.join(base_path, 'final_image.png'), float(noise_intensity_entry.value))
            else:
                extract_Frames.copy_image_with_new_name(os.path.join(base_path, 'out.png'), os.path.join(base_path, 'final_image.png'))

            print("Procesamiento de imagen terminado.")
            terminado.value = "Procesamiento de imagen terminado, puedes ver la imagen en la misma carpeta de este script con el nombre final_image.png."
            page.update()
    except Exception as err:
        error_message.value = f"Error: {err}"
        page.update()
    

if __name__ == "__main__":
    ft.app(target=main)

