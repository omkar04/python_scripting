import time
def monitor_log_for_keyword(log_file, keyword):
    with open(log_file, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line and keyword in line:
                print(f"Keyword found: {line}")
                # Trigger any action here
            time.sleep(1)


# Example Usage
monitor_log_for_keyword(r'E:\Task_01\backup_02\myapp\myapp.log', 'ERROR')
