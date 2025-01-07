import os
import subprocess

def compress_large_file(directory):
    for filename in os.listdir(directory):
        file_path=os.path.join(directory,filename)
        if os.path.getsize(file_path)>1:
            subprocess.run(['tar', '-czf', f'{file_path}.tar.gz', file_path])
            print(f"Compressed {filename}")

compress_large_file(r'E:\Task_01\backup_02\myapp')