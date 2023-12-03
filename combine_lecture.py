import os

# Path to the folder containing the Markdown files
folder_path = 'LectureSlides'

# List of your Markdown files, assuming they are named sequentially or have a specific pattern
markdown_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.md')])
print(markdown_files)
# Combined content
combined_content = ""

# Week counter
week_counter = 0
# Check if there are any files at all
if not markdown_files:
    print("No markdown files found in the directory.")
else:
    # Loop through all the files
    for file_name in markdown_files:
        # Adding a week header for each file
        combined_content += f"## Week {week_counter}\n\n"

        # Reading and adding the content of the file
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as f:
            combined_content += f.read() + "\n\n"

        # Special handling for Week 8 (increment week counter after one file)
        if week_counter == 8:
            week_counter += 1
        else:
            # Regular handling for other weeks (increment week counter after two files)
            if file_name != markdown_files[0] and (markdown_files.index(file_name) % 2 != 0):
                week_counter += 1

    # Path for the output file
    output_file_path = 'Lectures.md'

    # Write the combined content to a new Markdown file
    with open(output_file_path, 'w') as f:
        f.write(combined_content)

    print("Markdown files combined successfully with individual week headers for each lecture.")