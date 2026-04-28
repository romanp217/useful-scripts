import shutil
import os
import datetime

def backup_folder(source, destination):
    if not os.path.exists(source):
        print(f"Source folder '{source}' does not exist.")
        return
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_folder = os.path.join(destination, f"backup_{timestamp}")
    shutil.copytree(source, dest_folder)
    print(f"Backup created at {dest_folder}")

if __name__ == "__main__":
    src = input("Enter source folder path: ")
    dst = input("Enter destination folder path: ")
    backup_folder(src, dst)
