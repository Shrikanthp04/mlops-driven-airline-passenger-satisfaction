import os
import sys
import logging
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join("logs", LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] [%(module)s] : %(message)s",
    handlers=[
        logging.FileHandler(logs_path),
        logging.StreamHandler(sys.stdout)
        ]
    )

logger = logging.getLogger("Airline Passenger Reviews Logger")