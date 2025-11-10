thonimport json

def load_settings(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)