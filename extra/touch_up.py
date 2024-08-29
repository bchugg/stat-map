import os 
import re 

def reformat_math(file_path):
    # Open the file and read all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a list to store the updated lines
    updated_lines = []

    # Iterate through each line in the file
    for line in lines:
        # Check if the line includes $$ 
        if line.strip().includes('$$') and len(line.strip()) > 2:
            if line.strip().startswith('$$'): 
                # Add space after $$
                content = line.strip()[2:].strip()
                updated_lines.append(f"$$\n{content}\n")
            else: 
                # Add space before $$
                content = line.strip()[:-2].strip()
                updated_lines.append(f"{content}\n$$\n")

    # Write the updated lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

def reformat_subsection_links(file_path): 
    # Open the file and read all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a pattern to match [[<content1>#<content2>]]
    pattern = re.compile(r'\[\[(.+?)#(.+?)\]\]')

    # Create a list to store the updated lines
    updated_lines = []

    # Iterate through each line in the file
    for line in lines:
        # Search for the pattern in the line
        matches = pattern.findall(line)
        if matches:
            # Replace each match with the desired format
            for match in matches:
                content1, content2 = match
                replacement = f"[[{content1}#{content2}|{content1}:{content2}]]"
                line = line.replace(f"[[{content1}#{content2}]]", replacement)
        # Add the updated line to the list
        updated_lines.append(line)

    # Write the updated lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

def add_space_to_header(file_path):
    # Open the file and read all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a list to store the updated lines
    updated_lines = []

    # Iterate through each line in the file
    for line in lines:
        
        # Add current line 
        updated_lines.append(line)

        # Add space after line if it is a header
        if line.startswith('---'):
            updated_lines.append('\n')
        

    # Write the updated lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)


def replace_multiline_math(content):
    # Regex pattern to find occurrences of $$<content>$$, even if it spans multiple lines
    pattern = r'\$\$(.*?)\$\$'
    
    # Replace matched patterns with $$\n<content>\n$$
    replaced_content = re.sub(pattern, r'$$\n\1\n$$', content, flags=re.DOTALL)
    
    return replaced_content

def process_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Replace multiline math occurrences
    updated_content = replace_multiline_math(content)
    
    with open(file_path, 'w') as file:
        file.write(updated_content)


if __name__ == '__main__':
    # reformat markdown on all markdown files in content directory
    for file in os.listdir('../'):
        if file.endswith('.md'):
            # process_markdown_file(os.path.join('../', file))
            reformat_math(os.path.join('../', file))
            # reformat_latex(os.path.join('../', file))
            # reformat_subsection_links(os.path.join('../', file))
            #add_space_to_header(os.path.join('../', file))
