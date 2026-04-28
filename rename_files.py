import os

def rename_files(folder, prefix="new_"):
    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)
        if os.path.isfile(old_path):
            new_name = prefix + filename
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    prefix = input("Enter prefix (default 'new_'): ") or "new_"
    rename_files(folder, prefix)
