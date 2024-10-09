import os

def ensure_directory_exists(directory):
    """Ensure that the specified directory exists."""
    os.makedirs(directory, exist_ok=True)

def get_output_file_path(output_dir, model_name, extension):
    """Generate the full path for an output file."""
    return os.path.join(output_dir, f"{model_name}{extension}")

def read_file(file_path):
    """Read and return the contents of a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


