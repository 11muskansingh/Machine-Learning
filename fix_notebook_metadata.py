import nbformat
import os

def fix_notebook_metadata_in_dir(directory):
    for fname in os.listdir(directory):
        if fname.endswith(".ipynb"):
            nb_path = os.path.join(directory, fname)
            with open(nb_path, "r") as f:
                nb = nbformat.read(f, as_version=4)
            if "widgets" in nb["metadata"]:
                del nb["metadata"]["widgets"]
                print(f"Removed 'metadata.widgets' from {nb_path}")
            with open(nb_path, "w") as f:
                nbformat.write(nb, f)
    print("All notebooks in directory fixed.")

if __name__ == "__main__":
    fix_notebook_metadata_in_dir(os.getcwd())