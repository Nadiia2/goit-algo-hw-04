import os
import shutil
import argparse

def copy_files(source_dir, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            _, extension = os.path.splitext(file)
            destination_subdir = os.path.join(destination_dir, extension[1:])
            os.makedirs(destination_subdir, exist_ok=True)
            shutil.copy(source_file_path, destination_subdir)

def main():
    parser = argparse.ArgumentParser(description="Copy and sort files by extension.")
    parser.add_argument("source_dir", help="Path to the source directory.")
    parser.add_argument("destination_dir", nargs="?", default="dist", help="Path to the destination directory. Default is 'dist'.")
    args = parser.parse_args()


    if not os.path.exists(args.source_dir):
        print("Source directory does not exist.")
        return

    try:
        copy_files(args.source_dir, args.destination_dir)
        print("Files copied and sorted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
