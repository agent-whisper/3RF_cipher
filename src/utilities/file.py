import os

def read_byte(filedir):
    file_bytes = bytes('', 'utf-8')
    try:
        with open(filedir, 'rb') as f:
            for line in f.readlines():
                file_bytes += line
    except FileNotFoundError:
        print('[src.utilities.file.read_byte] file not found; returning empty string')
        return ''
    return file_bytes

def write_byte(data, output_dir):
    with open(output_dir, 'wb+') as f:
        f.write(data)

def create_folder(dir):
    try:
        os.makedirs(dir)
    except FileExistsError:
        pass