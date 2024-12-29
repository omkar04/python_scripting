import subprocess

def Check_service_status(service):
    # Use PowerShell to check service status
    result = subprocess.run(['powershell', '-Command', f"Get-Service {service}"], capture_output=True, text=True)
    
    if "Running" not in result.stdout:
        print(f"Service {service} is not running.")
        restart_service(service)
    else:
        print(f"Service {service} is running.")

def restart_service(service):
    # Use PowerShell to restart the service
    subprocess.run(['powershell', '-Command', f"Restart-Service {service}"])
    print(f"Service {service} restarted.")

Check_service_status('Fax')
