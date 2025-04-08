import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(os.path.dirname(logs_path),exist_ok=True)#keep on appending the logs to the file

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s]: %(lineno)d %(name)s-%(levelname)s- %(message)s',
    level=logging.INFO,
    filemode='a' #append mode
)

if __name__=="__main__":
    logging.info("Logging has started")
    logging.info("Logging has ended")