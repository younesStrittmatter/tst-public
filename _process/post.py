
import jinja2
from jinja2 import Template
import yaml
import json
import os
import re

# Directory paths
SOURCE_DIR = "./website/build/html/content"
BUILD_DIR = "./website"
JUPYTER_BOOK_BUILD_CMD = ["jupyter-book", "build", "_website_build"]
PUBLISH_CMD = "ghp-import -n -p -f _website_build/_build/html"

root = "website"

skip_dirs = ["_build"]

def replace_colab_link(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        pattern = r"https://colab\.research\.google\.com/github/([^/]+)/([^/]+)/blob/master/website/(.+)"
        replacement = r"https://colab.research.google.com/github/\1/\2/blob/gh-pages/sources/\3"
        replaced = re.sub(pattern, replacement, content)
    with open(file_path, "w") as f:
        f.write(replaced)
def build():
    # copy_if_changed(SOURCE_DIR, BUILD_DIR)
    #
    # _d = None
    # with open(f"{BUILD_DIR}/_config.yml") as f:
    #     _d = yaml.safe_load(f)
    #     _d["repository"]["path_to_book"] = "_book_build"
    #
    # yaml.safe_dump(_d, open(f"{BUILD_DIR}/_config.yml", "w"))

    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith(".html"):
                replace_colab_link(os.path.join(root, file))



def main():
    # args = sys.argv[1:]
    build()
    # if '--a' in args:
    #     build()
    #     subprocess.run(JUPYTER_BOOK_BUILD_CMD)
    #     subprocess.run(PUBLISH_CMD, shell=True)
    # else:
    #     build()


if __name__ == '__main__':
    main()


"https://colab.research.google.com/github/PrincetonUniversity/NEU-PSY-502/blob/master/website/content/502B/Primers/notebooks/1 Scalars, Vectors, and Matrices.ipynb"

"https://colab.research.google.com/github/PrincetonUniversity/NEU-PSY-502/blob/gh-pages/_source/content/502B/Primers/notebooks/1 Scalars, Vectors, and Matrices.ipynb"