import json

def writefile(data_file : str, data : any):
    """
        data_file: The Path location you want the file to writen.
        data: The data you want to be inserted into the file.
    """
    with open(data_file, "w") as f:
        data = json.dump(data, f, indent=4)
    return data