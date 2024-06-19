from PIL import Image
import numpy as np
import time
import os

def pixelate(image_path, output_path, block_size, spacing, brightness_factor):
    with Image.open(image_path) as image:
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
        
        Image.fromarray(output_array).save(output_path)

#pixelate('image.png', 'output_image2.jpg', block_size=6, spacing=6, brightness_factor=1.5)

#comentar si quieres pixelear solo una imagen y descomentar lo de arriba
dir_path = './original_frames'
count = 0
#itera el directorio
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
        
for i in range(1, count+1):
    st = time.time()
    pixelate(f'./original_frames/{i}.png', f'./pixelated_frames/{i}.png', 8, 8, brightness_factor=1.8)
    print(f'Frame {i} pixelated and saved as ./pixelated_frames/{i}.png')
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
