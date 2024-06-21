from PIL import Image
import numpy as np
import os
import time
import random

''' parametros pixelate(image_path, output_path, block_size, spacing, brightness_factor, frame_number)
    image_path: ruta de la imagen a procesar
    output_path: ruta de la imagen de salida
    block_size: tamaño de los bloques
    spacing: espacio entre bloques
    brightness_factor: factor de brillo
    frame_number: número de frame
'''
def pixelate_glitch(image_path, output_path, block_size, spacing, brightness_factor, frame_number, glitch_frame_number, color):
    if color == 'blue':
        with Image.open(image_path) as image:
            blocks_across = image.width // block_size
            blocks_down = image.height // block_size
            image = image.resize((blocks_across, blocks_down), Image.NEAREST)
            image = image.convert('L').point(lambda x: min(255, x * brightness_factor)).convert('RGB')
            arr = np.array(image)
            new_width = blocks_across * (block_size + spacing)
            new_height = blocks_down * (block_size + spacing)
            output_array = np.zeros((new_height, new_width, 3), dtype=np.uint8)

            #define si un frame tiene glitch o no
            if frame_number % glitch_frame_number >= 0 and frame_number % glitch_frame_number <= 1:
                glitch_line = random.randint(0, blocks_down - 1)
                start_pos = random.randint(0, blocks_across - 1)  #posicion aleatoria de inicio
                line_length = blocks_across // 4  #longitud del glitch

                for y in range(blocks_down):
                    for x in range(blocks_across):
                        blue_intensity = arr[y, x, 0]
                        if y == glitch_line and start_pos <= x < start_pos + line_length:
                            #oscurese la linea creando un glitch
                            blue_intensity = max(0, blue_intensity + 100)
                            color = (blue_intensity, blue_intensity, 255)
                        else:
                            #color normal
                            color = (0, 0, blue_intensity) if blue_intensity < 155 else (blue_intensity, blue_intensity, 255)

                        start_x = x * (block_size + spacing)
                        start_y = y * (block_size + spacing)
                        end_x = start_x + block_size
                        end_y = start_y + block_size
                        output_array[start_y:end_y, start_x:end_x] = color
            else:
                for y in range(blocks_down):
                    for x in range(blocks_across):
                        blue_intensity = arr[y, x, 0]
                        color = (0, 0, blue_intensity) if blue_intensity < 155 else (blue_intensity, blue_intensity, 255)
                        start_x = x * (block_size + spacing)
                        start_y = y * (block_size + spacing)
                        end_x = start_x + block_size
                        end_y = start_y + block_size
                        output_array[start_y:end_y, start_x:end_x] = color

            Image.fromarray(output_array).save(output_path)
    elif color == 'red':
        with Image.open(image_path) as image:
            blocks_across = image.width // block_size
            blocks_down = image.height // block_size
            image = image.resize((blocks_across, blocks_down), Image.NEAREST)
            image = image.convert('L').point(lambda x: min(255, x * brightness_factor)).convert('RGB')
            arr = np.array(image)
            new_width = blocks_across * (block_size + spacing)
            new_height = blocks_down * (block_size + spacing)
            output_array = np.zeros((new_height, new_width, 3), dtype=np.uint8)
            
            #define si un frame tiene glitch o no
            if frame_number % glitch_frame_number >= 0 and frame_number % glitch_frame_number <= 1:
                glitch_line = random.randint(0, blocks_down - 1)
                start_pos = random.randint(0, blocks_across - 1)  #posicion aleatoria de inicio
                line_length = blocks_across // 4  #longitud del glitch
    
                for y in range(blocks_down):
                    for x in range(blocks_across):
                        red_intensity = arr[y, x, 0]
                        if y == glitch_line and start_pos <= x < start_pos + line_length:
                            #oscurese la linea creando un glitch
                            red_intensity = max(0, red_intensity + 100)
                            color = (255, red_intensity, red_intensity)
                        else:
                            #color normal
                            color = (red_intensity, 0, 0) if red_intensity < 155 else (255, red_intensity, red_intensity)
                        
                        start_x = x * (block_size + spacing)
                        start_y = y * (block_size + spacing)
                        end_x = start_x + block_size
                        end_y = start_y + block_size
                        output_array[start_y:end_y, start_x:end_x] = color
            else:
                for y in range(blocks_down):
                    for x in range(blocks_across):
                        red_intensity = arr[y, x, 0]
                        color = (red_intensity, 0, 0) if red_intensity < 155 else (255, red_intensity, red_intensity)
                        start_x = x * (block_size + spacing)
                        start_y = y * (block_size + spacing)
                        end_x = start_x + block_size
                        end_y = start_y + block_size
                        output_array[start_y:end_y, start_x:end_x] = color
            
            Image.fromarray(output_array).save(output_path)
    elif color == 'green':
        with Image.open(image_path) as image:
            blocks_across = image.width // block_size
            blocks_down = image.height // block_size
            image = image.resize((blocks_across, blocks_down), Image.NEAREST)
            image = image.convert('L').point(lambda x: min(255, x * brightness_factor)).convert('RGB')
            arr = np.array(image)
            new_width = blocks_across * (block_size + spacing)
            new_height = blocks_down * (block_size + spacing)
            output_array = np.zeros((new_height, new_width, 3), dtype=np.uint8)
            
            #define si un frame tiene glitch o no
            if frame_number % glitch_frame_number >= 0 and frame_number % glitch_frame_number <= 1:
                glitch_line = random.randint(0, blocks_down - 1)
                start_pos = random.randint(0, blocks_across - 1)  #posicion aleatoria de inicio
                line_length = blocks_across // 4  #longitud del glitch
    
                for y in range(blocks_down):
                    for x in range(blocks_across):
                        green_intensity = arr[y, x, 0]
                        if y == glitch_line and start_pos <= x < start_pos + line_length:
                            #oscurese la linea creando un glitch
                            green_intensity = max(0, green_intensity + 100)
                            color = (green_intensity, 255, green_intensity)
                        else:
                            #color normal
                            color = (0, green_intensity, 0) if green_intensity < 155 else (green_intensity, 255, green_intensity)
                        
                        start_x = x * (block_size + spacing)
                        start_y = y * (block_size + spacing)
                        end_x = start_x + block_size
                        end_y = start_y + block_size
                        output_array[start_y:end_y, start_x:end_x] = color
            else:
                for y in range(blocks_down):
                    for x in range(blocks_across):
                        green_intensity = arr[y, x, 0]
                        color = (0, green_intensity, 0) if green_intensity < 155 else (green_intensity, 255, green_intensity)
                        start_x = x * (block_size + spacing)
                        start_y = y * (block_size + spacing)
                        end_x = start_x + block_size
                        end_y = start_y + block_size
                        output_array[start_y:end_y, start_x:end_x] = color
            
            Image.fromarray(output_array).save(output_path)
""" dir_path = './original_frames'
count = 0
#Itera el directorio para contar los archivos
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1

#Procesa cada frame
for i in range(1, count + 1):
    st = time.time()
    pixelate_glitch(f'{dir_path}/{i}.png', f'./pixelated_Frames/{i}.png', 8, 8, 1.7, i - 1, 30)
    et = time.time()
    print(f'Frame {i} pixelated and saved as ./pixelated_frames/{i}.png with execution time: {et - st} seconds')
 """