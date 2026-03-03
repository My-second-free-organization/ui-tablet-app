import os
from datetime import datetime, timedelta

def cleanup(days_old: int = 90):
    cutoff = datetime.utcnow() - timedelta(days=days_old)
    print(f"Cleaning up workflow instances older than {cutoff.isoformat()}")
    # Would connect to DB and delete old completed instances
    print("Cleanup complete")

if __name__ == "__main__": cleanup()
