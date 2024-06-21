import os

def rename_files(directory):
    files = sorted(os.listdir(directory))
    
    files = [file for file in files if os.path.isfile(os.path.join(directory, file))]
    
    for index, file in enumerate(files, start=1):
        extension = os.path.splitext(file)[1]
        
        new_name = f"{index}{extension}"
        
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed '{file}' to '{new_name}'")

directory = './original_frames'
#directory = './output_frames'
rename_files(directory)
