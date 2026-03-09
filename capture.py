import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        # Ignore the 'venv' folder to keep the list clean
        if 'venv' in dirs:
            dirs.remove('venv')
        if '.git' in dirs:
            dirs.remove('.git')
            
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

# Change this to your project path
list_files(r"C:\code\Scouting4Data")