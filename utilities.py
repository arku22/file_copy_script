from pathlib import Path
import os


def format_set_to_txt(files_set, output_txt_file):
    object_path = Path(".", output_txt_file)
    if os.path.exists(object_path):
        os.remove(object_path)

    for item in files_set:
        with open(output_txt_file, 'a') as f:
            f.write(str(item)+'\n')
    return
