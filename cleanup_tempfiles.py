import os
import time

def cleanup_tempfile(directory):
    current_time = time.time()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            # Check if the file is older than 7 days
            if os.path.getmtime(file_path) < current_time - 1 * 86400:
                # Delete the file or directory
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
                    print(f"Deleted directory: {file_path}")
        except PermissionError:
            print(f"Permission denied: {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")


cleanup_tempfile(r'C:\Windows\Temp')