import subprocess
import os
from datetime import datetime

def backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"flowforge_backup_{timestamp}.sql"
    cmd = f"pg_dump {os.getenv('DATABASE_URL')} > /backups/{filename}"
    subprocess.run(cmd, shell=True, check=True)
    print(f"Backup created: {filename}")

if __name__ == "__main__": backup()
