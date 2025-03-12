import zipfile
import os

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

# Example usage
if __name__ == "__main__":
    # Path to the ZIP file
    zip_file = r'my_files.zip'  # Replace with the path to your ZIP file

    # Directory to extract the contents
    extract_directory = r'extracted_files1'  # Replace with your desired extraction directory

    # Call the function to extract the ZIP file
    extract_zip(zip_file, extract_directory)