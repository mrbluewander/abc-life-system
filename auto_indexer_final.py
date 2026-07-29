
import os

def scan_md_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, encoding="utf-8") as file:
                    lines = file.readlines()
                    if lines:
                        if not lines[0].lstrip().startswith("#"):
                            title = filename.split(".")[0]
                        else:
                            title = lines[0].lstrip().strip("#").strip()
                        print(f"Title: {title}")
                        print(f"File: {filename}")
                    else:
                        print(f"File {filename} is empty")
            except OSError as e:
                print(f"Error reading file {filename}: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    scan_md_files(".")
