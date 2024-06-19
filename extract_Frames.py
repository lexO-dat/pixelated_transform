import imageio

def extract_frames(video_path, output_folder):
    reader = imageio.get_reader(video_path, 'ffmpeg')

    for i, frame in enumerate(reader):
        frame_filename = f"{output_folder}/frame_{i+1}.png"
        
        imageio.imwrite(frame_filename, frame)
        print(f"Frame {i+1} saved as {frame_filename}")

video_path = 'video.mp4'
output_folder = 'output_frames'
extract_frames(video_path, output_folder)
