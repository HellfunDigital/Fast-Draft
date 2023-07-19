```python
import os
import json

def load_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json_file(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def file_exists(filepath):
    return os.path.isfile(filepath)

def directory_exists(directory):
    return os.path.isdir(directory)

def create_directory(directory):
    if not directory_exists(directory):
        os.makedirs(directory)
```