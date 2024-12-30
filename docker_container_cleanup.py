import subprocess

def list_docker_containers():
   
    print("Listing all Docker containers:")
    result = subprocess.run(['docker', 'ps', '-a'], text=True, capture_output=True)
    print(result.stdout)  

def cleanup_docker():
    subprocess.run(['docker', 'container', 'prune', '-f'])
    print("unused docker container removed")


cleanup_docker()