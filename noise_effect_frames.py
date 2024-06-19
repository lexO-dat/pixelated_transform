from PIL import Image
import numpy as np
import os
from multiprocessing import Pool

def apply_static_noise(image_path, output_path, noise_intensity):
    with Image.open(image_path) as image:
        arr = np.array(image)
        
        noise = (np.random.rand(*arr.shape) - 0.5) * 255 * 2 * noise_intensity
        noisy_image = np.clip(arr + noise, 0, 255).astype(np.uint8)
        
        Image.fromarray(noisy_image).save(output_path)

def process_image(params):
    file_path, output_folder, noise_intensity = params
    if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        file_name = os.path.basename(file_path)
        output_file_path = os.path.join(output_folder, file_name)
        apply_static_noise(file_path, output_file_path, noise_intensity)
        print(f"Processed {file_name} with noise added.")

def process_folder(input_folder, output_folder, noise_intensity):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    tasks = [(os.path.join(input_folder, f), output_folder, noise_intensity) for f in os.listdir(input_folder)]
    
    with Pool() as pool:
        pool.map(process_image, tasks)

if __name__ == '__main__':
    input_folder = './pixelated_frames' 
    output_folder = './final_frames'      
    noise_intensity = 0.2         

    process_folder(input_folder, output_folder, noise_intensity)
