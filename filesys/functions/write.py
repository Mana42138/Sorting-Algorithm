from functions.devs_defaults_v1 import *

def writefile(data_file, data):
    """
    data_file: The path location you want the file to be written.
    data: The data you want to be inserted into the file.
    """
    full_path = os.path.abspath(data_file)
    directory = os.path.dirname(full_path)

    os.makedirs(directory, exist_ok=True)

    with open(full_path, "w") as f:
        json.dump(data, f, indent=4)


def makefolder(folder_path):
    """
    folder_path: The path you want to place the desired folder.
    """
    full_path = os.path.abspath(folder_path)
    # directory = os.path.dirname(full_path)

    os.makedirs(full_path, exist_ok=True)
    