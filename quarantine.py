import os
import shutil
from datetime import datetime

QUARANTINE_DIR = "data/quarantine"

def quarantine_file(filepath):
    os.makedirs(QUARANTINE_DIR, exist_ok=True)

    filename = os.path.basename(filepath)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_name = f"{timestamp}_{filename}"

    dest_path = os.path.join(QUARANTINE_DIR, new_name)
    shutil.move(filepath, dest_path)