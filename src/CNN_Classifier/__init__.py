import os
import sys
import logging

log_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    handlers=[
        logging.FileHandler(log_filepath, mode='a'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("CNN_Classifier")