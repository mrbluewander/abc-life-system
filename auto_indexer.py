Here is the Python script that meets the specifications:
```
import os

def generate_index():
    # Scan current directory
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.endswith(".md"):
            with open(filename, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
            file_path = os.path.join(current_dir, filename)
            title = first_line[1:] if first_line.startswith("#") else first_line
            yield title, filename

def write_index(index_filename, data):
    with open(index_filename, 'w', encoding='utf-8') as f:
        f.write("# Index\n")
        for title, filename in data:
            f.write(f"* [{title}]({filename})\n")

def main():
    index_data = list(generate_index())
    write_index('INDEX.md', index_data)
    print("INDEX.md generated successfully.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        print("Error generating INDEX.md. Please check the script and try again.")
```
This script should meet all the requirements specified, including error handling. Let me know if you need any further modifications or if you'd like me to explain any part of the code!