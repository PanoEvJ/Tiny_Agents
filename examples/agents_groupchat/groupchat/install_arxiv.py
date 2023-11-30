# filename: install_arxiv.py

import subprocess

try:
    subprocess.check_call(["pip", "install", "arxiv"])
except Exception as e:
    print(f"An error occurred while installing the 'arxiv' library: {str(e)}")