import logging 
import os
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG_FILE = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'
LOGS_DIR = os.path.join(ROOT_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)