# security.py
import os
import platform
import subprocess

class SystemSecurity:
    def get_system_info(self):
        info = {
            "os": platform.system(),
            "os_version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor()
        }
        return info

    def check_for_vulnerabilities(self):
        vulnerabilities = []
        
        if platform.system() == "Windows":
            result = subprocess.run(["wmic", "qfe"], capture_output=True, text=True)
            if "No Instance(s) Available" in result.stdout:
                vulnerabilities.append("Система не обновлена.")
        
        return vulnerabilities

    def fix_vulnerabilities(self):
        if platform.system() == "Windows":
            subprocess.run(["powershell", "Install-WindowsUpdate"], shell=True)
