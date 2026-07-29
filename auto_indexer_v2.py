import os
import glob

try:
    index_file = open('INDEX.md', 'w')
    index_file.write('# Index\n\n')

    md_files = glob.glob('*.md')
    md_files.sort()

    for file in md_files:
        if file != 'INDEX.md':
            try:
                with open(file, 'r') as f:
                    title = f.readline().strip()
                    index_file.write(f'* [{title}]({file})\n')
            except Exception as e:
                print(f'Error reading {file}: {e}')

    index_file.close()
    print('INDEX.md generated successfully')

except Exception as e:
    print(f'Error generating INDEX.md: {e}')