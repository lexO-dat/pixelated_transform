from PIL import Image
import numpy as np
import time
import os

''' parametros pixelate(image_path, output_path, block_size, spacing, brightness_factor, frame_number)
    image_path: ruta de la imagen a procesar
    output_path: ruta de la imagen de salida
    block_size: tamaño de los bloques
    spacing: espacio entre bloques
    brightness_factor: factor de brillo
'''
def pixelate(image_path, output_path, block_size, spacing, brightness_factor):
    #Abre la imagen desde el path especificado
    with Image.open(image_path) as image:
        #Calcula cuántos bloques caben horizontal y verticalmente basados en el tamaño del bloque
        blocks_across = image.width // block_size
        blocks_down = image.height // block_size
        
        #Redimensiona la imagen a la cantidad de bloques
        image = image.resize((blocks_across, blocks_down), Image.NEAREST)
        
        #Convierte la imagen a escala de grises, ajusta el brillo, y vuelve a convertirla a RGB
        image = image.convert('L').point(lambda x: min(255, x * brightness_factor)).convert('RGB')
        
        #Convierte la imagen a un array de numpy para manipulación de píxeles
        arr = np.array(image)
        
        #Calcula las nuevas dimensiones de la imagen, teniendo en cuenta el espacio entre bloques
        new_width = blocks_across * (block_size + spacing)
        new_height = blocks_down * (block_size + spacing)
        output_array = np.zeros((new_height, new_width, 3), dtype=np.uint8)
        
        #Proceso de asignación de colores a los bloques
        for y in range(blocks_down):
            for x in range(blocks_across):
                blue_intensity = arr[y, x, 0]
                #mientras menor el numero al que se compara la intensidad mas oscura termina siendo la foto
                color = (0, 0, blue_intensity) if blue_intensity < 155 else (blue_intensity, blue_intensity , 255)
                start_x = x * (block_size + spacing)
                start_y = y * (block_size + spacing)
                end_x = start_x + block_size
                end_y = start_y + block_size
                
                output_array[start_y:end_y, start_x:end_x] = color
        
        #Guarda la imagen procesada en el path especificado
        Image.fromarray(output_array).save(output_path)


#pixelate('./examples/image.png', 'output.jpg', 6, 6, 1.2)

#comentar si quieres pixelear solo una imagen y descomentar lo de arriba
dir_path = './original_frames'
count = 0
#itera el directorio
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
        
for i in range(1, count+1):
    st = time.time()
    pixelate(f'./original_frames/{i}.png', f'./pixelated_frames/{i}.png', 3, 3, 1.3)
    print(f'Frame {i} pixelated and saved as ./pixelated_frames/{i}.png')
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
