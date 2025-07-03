import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "CNN-Classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir = file_path.parent
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
        logging.info(f"Creating directory: {file_dir}")
    
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")