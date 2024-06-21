from extract_Frames import extract_frames
from frames_to_mp4 import create_video_from_frames
from noise_effect_frames import process_folder
from pixelate import pixelate
from pixelate_glitch import pixelate_glitch
from rename_files import rename_files
import os

'''
extract_frames('vide_path', 'output_folder')
frames_to_mp4('frame_folder', 'output_path', 'output_video_name')
process_folder('input_folder', 'output_folder', noise_intensity)
pixelate('input_folder', 'output_folder', block_size, space, brightness) -> process a folder of images
pixelate_glitch('input_folder', 'output_folder', block_size, space, brightness, i - 1 -> frame that will be glitched)
rename_files('directory')
'''

#main loop
video_name = input("enter the video name (it should be in the same folder as this script): ")
output_folder = input("enter the exact output location path (./ for this script folder): ")

glitch = input("do you want to glitch the video? (y/n): ")
if(glitch == 'y' or glitch == 'Y'):
    glitch_frame_number = int(input("enter the glitch frame number, greater the number less glitch (recommend 10 - 40): "))
    block_size = int(input("enter the block size: "))
    space = int(input("enter the spacing (recommend the same number as the block_size): "))
    brightness = float(input("enter the brightness factor (it depends of the video i recomend values between 1.1 and 1.7): "))
else:
    block_size = int(input("enter the block size: "))
    space = int(input("enter the spacing (recommend the same number as the block_size): "))
    brightness = float(input("enter the brightness factor (it depends of the video i recomend values between 1.1 and 1.7): "))

noise = input("do you want to add noise to the video? (y/n): ")
if(noise == 'y' or noise == 'Y'):
    noise_intensity = float(input("enter the noise intensity (recommend 0.1 - 0.5): "))

extract_frames(f'./{video_name}', './original_frames')

if(glitch == 'y'):
    count = 0
    for path in os.listdir('./original_frames'):
        if os.path.isfile(os.path.join('./original_frames', path)):
            count += 1

    for i in range(1, count + 1):
        pixelate_glitch('./original_frames', './pixelated_frames', block_size, space, brightness, i - 1, glitch_frame_number)
        print(f'Frame {i} pixelated')
else:
    count = 0
    for path in os.listdir('./original_frames'):
        if os.path.isfile(os.path.join('./original_frames', path)):
            count += 1

    for i in range(1, count + 1):
        pixelate('./original_frames', './pixelated_frames', block_size, space, brightness)
        print(f'Frame {i} pixelated')

if(noise == 'y'):
    process_folder('./pixelated_frames', './final_frames', noise_intensity)

create_video_from_frames('./final_frames', output_folder, 'final_video.mp4')