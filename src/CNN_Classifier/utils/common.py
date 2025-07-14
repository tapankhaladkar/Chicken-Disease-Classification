import os
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
import base64
from pathlib import Path
from CNN_Classifier import logger


@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (str): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except FileNotFoundError as e:
        logger.error(f"File not found: {path_to_yaml}")
        raise e
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {e}")
        raise e
    


@ensure_annotations
def create_directories(paths: list, verbose=True):
    """
    Creates directories if they do not exist.
    
    Args:
        paths (list): List of directory paths to create.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")



@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.
    
    Args:
        path (str): Path to the JSON file.
        data (dict): Data to save.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"Saved data to {path}")



@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a dictionary from a JSON file.
    
    Args:
        path (str): Path to the JSON file.
        
    Returns:
        dict: Loaded data.
    """
    with open(path, "r") as json_file:
        data = json.load(json_file)
    logger.info(f"Loaded data from {path}")
    return ConfigBox(data)  


@ensure_annotations
def save_bin(path: Path, data: Any):
    """
    Saves data to a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        data (Any): Data to save.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Saved data to {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        
    Returns:
        Any: Loaded data.
    """
    data = joblib.load(filename=path)
    logger.info(f"Loaded data from {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> int:
    """
    Gets the size of a file in bytes.
    
    Args:
        path (Path): Path to the file.
        
    Returns:
        int: Size of the file in bytes.
    """
    size = path.stat().st_size
    logger.info(f"Size of {path}: {size} bytes")
    return size


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())