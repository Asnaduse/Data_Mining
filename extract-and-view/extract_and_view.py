import zipfile
import os
import subprocess

def extract_zip(zip_path, extract_to):
    """
    Extracts a ZIP file to a specified directory.

    :param zip_path: Path to the ZIP file.
    :param extract_to: Directory where the contents will be extracted.
    """
    # Check if the ZIP file exists
    if not os.path.exists(zip_path):
        print(f"Error: ZIP file not found - {zip_path}")
        return

    # Create the extraction directory if it doesn't exist
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
        print(f"Created directory: {extract_to}")

    # Extract the ZIP file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted {zip_path} to {extract_to}")

def display_text_file(file_path):
    """
    Displays the contents of a text file.

    :param file_path: Path to the text file.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return

    print(f"\nContents of {os.path.basename(file_path)}:")
    with open(file_path, 'r', encoding='utf-8') as file:
        print(file.read())

def open_image_file(file_path):
    """
    Opens an image file using the default image viewer.

    :param file_path: Path to the image file.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return

    print(f"\nOpening {os.path.basename(file_path)}...")
    if os.name == 'nt':  # Windows
        os.startfile(file_path)
    elif os.name == 'posix':  # macOS or Linux
        subprocess.run(['open', file_path] if os.uname().sysname == 'Darwin' else ['xdg-open', file_path])
    else:
        print("Unsupported operating system. Please open the file manually.")

def find_files_in_directory(directory, file_names):
    """
    Searches for files in a directory and its subdirectories.

    :param directory: Directory to search in.
    :param file_names: List of file names to search for.
    :return: Dictionary mapping file names to their full paths.
    """
    found_files = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file in file_names:
                found_files[file] = os.path.join(root, file)
    return found_files

# Example usage
if __name__ == "__main__":
    # Path to the ZIP file
    zip_file = r'my_files.zip'  # Replace with the path to your ZIP file

    # Directory to extract the contents
    extract_directory = r'extracted_files'  # Replace with your desired extraction directory

    # Call the function to extract the ZIP file
    extract_zip(zip_file, extract_directory)

    # Search for the files in the extracted directory
    files_to_find = ['file1.txt', 'file2.png']
    found_files = find_files_in_directory(extract_directory, files_to_find)

    # Display the contents of the text file
    if 'file1.txt' in found_files:
        display_text_file(found_files['file1.txt'])
    else:
        print("Error: file1.txt not found in the extracted files.")

    # Open the image file
    if 'file2.png' in found_files:
        open_image_file(found_files['file2.png'])
    else:
        print("Error: file2.png not found in the extracted files.")