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
    # Process the first file for Week 0
    first_file_path = os.path.join(folder_path, markdown_files[0])
    combined_content += f"## Week {week_counter}\n\n"
    with open(first_file_path, 'r') as f:
        combined_content += f.read() + "\n\n"
    week_counter += 1

    # Loop through the rest of the files
    i = 1
    while i < len(markdown_files):
        # Adding a week header
        combined_content += f"## Week {week_counter}\n\n"

        # Special handling for Week 8 and Week 9 (one file each)
        if week_counter in [8]:
            file_path = os.path.join(folder_path, markdown_files[i])
            with open(file_path, 'r') as f:
                combined_content += f.read() + "\n\n"
            i += 1  # Increment file index by 1

        # Regular handling for other weeks (two files each)
        else:
            for j in range(2):
                if i + j < len(markdown_files):
                    file_path = os.path.join(folder_path, markdown_files[i + j])
                    with open(file_path, 'r') as f:
                        combined_content += f.read() + "\n\n"
            i += 2  # Increment file index by 2

        # Increment the week counter
        week_counter += 1

        # Ensure that the week counter does not exceed 10
        if week_counter > 11:
            break

    # Path for the output file
    output_file_path = 'Lectures.md'

    # Write the combined content to a new Markdown file
    with open(output_file_path, 'w') as f:
        f.write(combined_content)

    print("Markdown files combined successfully with week headers.")
