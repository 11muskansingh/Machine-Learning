import nbformat
import sys
import os

def fix_widgets_metadata(nb_path):
    nb = nbformat.read(nb_path, as_version=nbformat.NO_CONVERT)
    if 'widgets' in nb.metadata:
        widgets = nb.metadata['widgets']
        if 'state' not in widgets:
            widgets['state'] = {}
            print(f"Added empty 'state' key to metadata.widgets in {nb_path}.")
        nb.metadata['widgets'] = widgets
    nbformat.write(nb, nb_path)
    print(f"Notebook metadata fixed: {nb_path}")

def fix_all_ipynb_in_dir(directory):
    for fname in os.listdir(directory):
        if fname.endswith('.ipynb'):
            fix_widgets_metadata(os.path.join(directory, fname))

if __name__ == "__main__":
    # If a directory is provided, fix all .ipynb files in it, else use current directory
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = os.getcwd()
    if not os.path.isdir(target_dir):
        print(f"Directory not found: {target_dir}")
        sys.exit(1)
    fix_all_ipynb_in_dir(target_dir)

# To run the script for all notebooks in the current directory:
# python fix_notebook_metadata.py
# Or for a specific directory:
# python fix_notebook_metadata.py "<directory_path>"
# Example:
# python fix_notebook_metadata.py "/workspaces/Machine-Learning/Classification/Titanic Ship Survival"
