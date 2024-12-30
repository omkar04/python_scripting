import os
import time
import glob

def rotate_log(LOG_PATTERN):
    for log_file in glob.glob(LOG_PATTERN):
        if os.path.getsize(log_file) > 5:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            os.rename(log_file, f"{timestamp}_{log_file}")
            open(log_file, 'w').close()
            print(f"log rotated: {log_file}")

rotate_log(r'E:\Task_01\backup_02\myapp\*.log')
  