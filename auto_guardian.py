import os, time, subprocess, logging, psutil
from pathlib import Path

REPO_PATH = Path(r"C:\Users\002\ghost-fleet-hq\abc-life-system")
LOG_FILE = REPO_PATH / "guardian_log.txt"
MEMORY_LIMIT_PERCENT = 85

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()]
)

def check_system_health():
    try:
        mem = psutil.virtual_memory()
        if mem.percent > MEMORY_LIMIT_PERCENT:
            logging.warning(f"⚠️ Memory High ({mem.percent}%). Pausing.")
            return False
    except:
        pass
    return True

def main_loop():
    logging.info("🛡️ Auto-Guardian Started.")
    while True:
        try:
            os.chdir(REPO_PATH)
            if not check_system_health():
                time.sleep(60)
                continue
            subprocess.run(["git", "pull"], check=True, capture_output=True)
            task_files = list(REPO_PATH.glob("pending_*.py"))
            if task_files:
                for task in task_files:
                    if check_system_health():
                        logging.info(f"⚡ Executing: {task.name}")
                        result = subprocess.run(["python", str(task)], capture_output=True, text=True)
                        (REPO_PATH / "execution_result.md").write_text(result.stdout + "\n" + result.stderr)
                        subprocess.run(["git", "add", "."], check=True, capture_output=True)
                        subprocess.run(["git", "commit", "-m", f"Auto-exec: {task.name}"], check=True, capture_output=True)
                        subprocess.run(["git", "push"], check=True, capture_output=True)
                        task.unlink()
                        logging.info("✅ Task completed.")
                    else:
                        break
            else:
                logging.debug("No pending tasks.")
        except Exception as e:
            logging.error(f"Guardian Error: {e}")
        time.sleep(30)

if __name__ == "__main__":
    main_loop()