import subprocess

def pull_latest_code(repo_dir):
    result = subprocess.run(['git', 'pull'], cwd=repo_dir, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Code pulled successfully.")
        print(result.stdout)
    else:
        print("Error pulling code:")
        print(result.stderr)
repo_dir = r'E:\Task_01\backup_01'
pull_latest_code(repo_dir)