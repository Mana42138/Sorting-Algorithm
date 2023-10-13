import json

def readfile(data_file : str):
    """
        data_file: The file path you want to read.
    """
    with open(data_file, "r") as f:
        data = json.load(f)
    return data