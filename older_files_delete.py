import os
import time

def delete_files(directory):
    current_time= time.time()
    for filename in os.listdir(directory):
        file_path=os.path.join(directory,filename)
        if os.path.getmtime(file_path)< current_time-3*86400:
            os.remove(file_path)
            print(f"Delete{file_path}")

delete_files(r'E:\Task_01\backup_02\myapp')