import cv2
from PIL import Image
import numpy as np
import time

def pixelate(image, block_size, spacing, brightness_factor):
    blocks_across = image.width // block_size
    blocks_down = image.height // block_size
    image = image.resize((blocks_across, blocks_down), Image.NEAREST)
    
    image = image.convert('L').point(lambda x: min(255, x * brightness_factor)).convert('RGB')
    
    arr = np.array(image)
    
    new_width = blocks_across * (block_size + spacing)
    new_height = blocks_down * (block_size + spacing)
    output_array = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    
    for y in range(blocks_down):
        for x in range(blocks_across):
            gray_value = arr[y, x, 0]
            blue_intensity = int((gray_value / 255) * 255)
            color = (0, 0, blue_intensity) if gray_value < 128 else (blue_intensity, blue_intensity, 255)
            
            start_x = x * (block_size + spacing)
            start_y = y * (block_size + spacing)
            end_x = start_x + block_size
            end_y = start_y + block_size
            
            output_array[start_y:end_y, start_x:end_x] = color
    
    return Image.fromarray(output_array)

def live_pixelate(block_size, spacing, brightness_factor):
    cap = cv2.VideoCapture(1)  #se inicia la camara (0 es el estandar pero en mi caso es 1)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        #se convierte la imagen ya que cv2 lee las imagenes en BGR y PIL en RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(frame)  # Convertir a imagen de PIL

        #se pixela la imagen con la funcion pixelate
        pixelated_image = pixelate(pil_img, block_size, spacing, brightness_factor)
        
        #se convierte la imagen de nuevo a BGR pasando la imagen primero a un array de numpy 
        cv2_frame = np.array(pixelated_image)
        cv2_frame = cv2.cvtColor(cv2_frame, cv2.COLOR_RGB2BGR)

        #se muestra el frame pixelado
        cv2.imshow('Pixelated Live Video', cv2_frame)

        #se sale con q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

#parametros: tamaño del pixel, espacio entre pixeles y factor de brillo
block_size = 6
spacing = 6
brightness_factor = 1.7

live_pixelate(block_size, spacing, brightness_factor)
