import glob
import os
import shutil


# Set paths
path_to_automation = "Automation_Files/*.py"
path_to_db_in_TBC = "Data_Processing_Script/TBC/*.db"
path_to_TBC = "Data_Processing_Script/TBC"
path_to_data = "Data_Processing_Script/"
path_to_data_csv = "Data_Processing_Script/*.csv"
path_to_data_db = "Data_Processing_Script/*.db"
path_to_data_old = "Data_Processing_Script/*.old"
path_to_comp_csv = "Data_Processing_Script/Complete/*.csv"

# Set files paths for scripts
bat_file_path = "Data_Processing_Script/DBRecovery.bat"
py_file_path = "Data_Processing_Script/main.py"
sqlite_file_path = "Data_Processing_Script/sqlite3.exe"

def check_path(path, file_ex):
    files = glob.glob(path)
    target_file = None
    # Find the first file with the specified extension
    for file in files:
        if file.endswith(file_ex):
            target_file = file
            print("Target file found: " + target_file)
            break  # stop after finding the first matching file
    exists = len(files) > 0
    print(f"Path: \"{path}\", Exists: {exists}, Number of files: {len(files)}")
    
# Methods for moving specific file types
def move_file_by_type(src, dst, file_extension):
    target_file = None
    # Find the first file with the specified extension
    for file in os.listdir(src):
        if file.endswith(file_extension):
            target_file = file
            print("Target file found: " + target_file)
            break  # stop after finding the first matching file
    
    # If file is found, move it to dst
    if target_file:
        src_path = os.path.join(src, target_file)
        dst_path = os.path.join(dst, target_file)
        shutil.move(src_path, dst_path)
        print(f"Moved {target_file} to {dst_path}")
    else:
        print(f"No {file_extension} file found in directory {src}")


