import cv2
from PIL import Image
import numpy as np
import os

# Leer la imagen de gradiente para crear el mapa de colores
gradient_img = np.array([[x for x in range(256)]] * 1, dtype='uint8')
colormap = cv2.applyColorMap(gradient_img, cv2.COLORMAP_JET)

def pixelate(image, block_size, spacing, colormap):
    blocks_across = image.width // block_size
    blocks_down = image.height // block_size
    new_width = blocks_across * (block_size + spacing)
    new_height = blocks_down * (block_size + spacing)

    # Reducir la imagen
    small_image = image.resize((blocks_across, blocks_down), Image.NEAREST)
    small_image = small_image.convert('L')

    small_pixels = np.array(small_image)
    
    # Crear la imagen final con el color transformado y espaciado
    final_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    
    for y in range(blocks_down):
        for x in range(blocks_across):
            gray_value = small_pixels[y, x]
            color = colormap[0, gray_value]  # Usar el valor de gris para obtener el color del mapa
            for dy in range(block_size):
                for dx in range(block_size):
                    final_y = y * (block_size + spacing) + dy
                    final_x = x * (block_size + spacing) + dx
                    if final_y < new_height - spacing and final_x < new_width - spacing:
                        final_image[final_y, final_x] = color

            # Añadir el espaciado
            for dy in range(block_size + spacing):
                for dx in range(block_size + spacing):
                    final_y = y * (block_size + spacing) + dy
                    final_x = x * (block_size + spacing) + dx
                    if dx >= block_size or dy >= block_size:
                        if final_x < new_width and final_y < new_height:
                            final_image[final_y, final_x] = (0, 0, 0)

    return Image.fromarray(final_image)

# Procesar una imagen de ejemplo para verificar el resultado
example_image = Image.open('./gradient_test/image.png')
pixelated_image = pixelate(example_image, 5, 5, colormap)
pixelated_image.show()
pixelated_image.save('pixelated_output.png')
