import cv2
import os

def create_video_from_frames(frame_folder, output_path, output_video_name, fps=30):
    frame_files = [os.path.join(frame_folder, f) for f in os.listdir(frame_folder) if f.endswith('.png')]
    frame_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))  # Ordenar archivos por número

    if not frame_files:
        raise ValueError("No frames found in the specified directory.")

    #Leer el primer cuadro para obtener el tamaño del video
    first_frame = cv2.imread(frame_files[0])
    if first_frame is None:
        raise ValueError("The first frame could not be read.")
    frame_height, frame_width = first_frame.shape[:2]

    #Inicializar el objeto VideoWriter con H.264 codec (para que sea compatible con la mayoría de los reproductores de video)
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    output_video_path = os.path.join(output_path, output_video_name)
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    for i, frame_file in enumerate(frame_files):
        frame = cv2.imread(frame_file)
        if frame is None:
            print(f"Warning: Skipping frame {frame_file} as it could not be read.")
            continue

        #verifica el tamaño del cuadro
        if frame.shape[:2] != (frame_height, frame_width):
            print(f"Warning: Frame {frame_file} has a different size and will be resized.")
            frame = cv2.resize(frame, (frame_width, frame_height))
        
        video_writer.write(frame)
        print(f'Frame {i + 1} of {len(frame_files)} written.')

    video_writer.release()
    print(f'Video output to {output_video_path}')

""" frame_folder = './pixelated_frames/'
output_path = './'
output_video_name = 'output.mp4'
create_video_from_frames(frame_folder, output_path, output_video_name)
 """