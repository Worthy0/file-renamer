import os
import re
import shutil

def normalize_filename(filename, replace_space_with, case_preference):
    name, ext = os.path.splitext(filename)
    if case_preference:
        name = name.lower()
    name = name.replace(' ', replace_space_with)
    name = re.sub(r'[^\w-]', '_', name.strip())
    return f"{name}{ext.lower()}"

def backup_directory(directory):
    backup_path = f"{directory}_backup"
    shutil.copytree(directory, backup_path)
    return backup_path

def rename_files_in_directory(directory, replace_space_with="_", case_preference=True):
    renamed_files = []
    errors = []
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path):
            try:
                new_filename = normalize_filename(filename, replace_space_with, case_preference)
                new_path = os.path.join(directory, new_filename)
                os.rename(old_path, new_path)
                renamed_files.append((filename, new_filename))
            except Exception as e:
                errors.append((filename, str(e)))
    return renamed_files, errors
