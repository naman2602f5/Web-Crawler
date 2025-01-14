import os
from logging.handlers import TimedRotatingFileHandler
import logging


log_format = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'

logging.basicConfig(level=logging.INFO, format=log_format)

logger = logging.getLogger("werkzeug")

log_directory = os.getcwd() + '/logs'
log_filename = 'application.log'
max_log_size = 10 * 1024 * 1024  # 1 MB
backup_count = 3  # Number of backup log files to keep

os.makedirs(log_directory, exist_ok=True)
handler = TimedRotatingFileHandler(os.path.join(log_directory, log_filename),
                                   when="MIDNIGHT", interval=1, backupCount=3)

handler.setLevel(logging.INFO)

formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)

logger.addHandler(handler)