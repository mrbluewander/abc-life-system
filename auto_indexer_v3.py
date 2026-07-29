
import os

# Initialize index content
index_content = ""

# Scan all .md files except INDEX.md
for filename in os.listdir():
    if filename.endswith(".md") and filename != "INDEX.md":
        with open(filename, "r", encoding="utf-8") as file:
            first_line = file.readline().strip()
            if not first_line or not first_line.startswith("#"):
                title = filename.replace(".md", "")
            else:
                title = first_line.replace("#", "").strip()
            index_content += f"- [{title}](./{filename})\n"

# Write INDEX.md with utf-8
with open("INDEX.md", "w", encoding="utf-8") as index_file:
    index_file.write("# Index\n\n")
    index_file.write(index_content)
