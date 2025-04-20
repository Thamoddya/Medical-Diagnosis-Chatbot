import os
from pathlib import Path
import logging

# LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='[$(asctime)s]: %(message)s:'
)

# FILE AND FOLDERS
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "README.md",
    "setup.py",
    "app.py",
    "research/trials.pipynb"
]

# LOGIC

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")
        
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating empty file {filename} in {filedir}")
    else:
        logging.info(f"File {filename} already exists in {filedir}")
    