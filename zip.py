import os
import zipfile

def zip_files_in_folder(folder_path, output_zip_file):
    # Create a ZipFile object
    with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through all files and directories in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Create the full file path
                full_path = os.path.join(root, file)
                # Write the file to the zip archive, preserving the directory structure
                arcname = os.path.relpath(full_path, start=folder_path)
                zipf.write(full_path, arcname)

# Example usage
folder_to_zip = 'output_scaled_images'
output_zip_file = 'output_filename.zip'

zip_files_in_folder(folder_to_zip, output_zip_file)
