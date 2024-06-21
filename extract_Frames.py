import imageio

def extract_frames(video_path, output_folder, obj):
    reader = imageio.get_reader(video_path, 'ffmpeg')

    for i, frame in enumerate(reader):
        frame_filename = f"{output_folder}/{i+1}.png"
        imageio.imwrite(frame_filename, frame)
        obj.terminado = f"Frame {i+1} saved as {frame_filename}"
        print(f"Frame {i+1} saved as {frame_filename}")
    
def extract_frame(video_path, output_folder, frame_number):
    reader = imageio.get_reader(video_path, 'ffmpeg')
    frame = reader.get_data(frame_number - 1)
    frame_filename = f"{output_folder}/preview.png"
    imageio.imwrite(frame_filename, frame)
    print(f"Frame 1 saved as {frame_filename}")
    reader.close()
    return

def ct_frames(video_path):
    reader = imageio.get_reader(video_path, 'ffmpeg')
    count = reader.count_frames()
    reader.close()
    return count

def copy_image_with_new_name(source_path, destination_path):
    #lee la imagen
    image = imageio.imread(source_path)
    #escribe la imagen
    imageio.imwrite(destination_path, image)

#video_path = './video.mp4'
#output_folder = './original_frames'
#extract_frames(video_path, output_folder)
