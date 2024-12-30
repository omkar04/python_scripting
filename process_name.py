import psutil
def check_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return True
    return False

if check_process('explorer.exe'):
    print("explorer.exe is runnning")
else:
    print("explorer.exe is not running")
    