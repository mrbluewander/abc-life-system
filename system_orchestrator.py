
import os
import sys
import time
import threading
import subprocess
import winreg
import shutil

# Constants
MEMORY_GUARDIAN_PATH = 'memory_guardian.py'
TXF_RISK_CALCULATOR_PATH = 'txf_risk_calculator.py'
GIT_REPO_PATH = 'path_to_your_git_repo'
SELF_HEAL_SCRIPT_PATH = 'self_heal_script.py'

def auto_start_on_boot():
    # Create a new task in Windows Task Scheduler
    subprocess.run([
        'schtasks',
        '/create',
        '/tn',
        'System Orchestrator',
        '/tr',
        sys.executable + ' ' + __file__,
        '/sc',
        'onstart',
        '/rl',
        'highest'
    ])

def monitor_and_restart_memory_guardian():
    while True:
        # Check if memory_guardian.py is running
        running_processes = subprocess.check_output(['tasklist']).decode('utf-8')
        if MEMORY_GUARDIAN_PATH not in running_processes:
            # Restart memory_guardian.py if it's not running
            subprocess.Popen([sys.executable, MEMORY_GUARDIAN_PATH])
        time.sleep(60)

def auto_detect_blue_screen_logs():
    while True:
        # Use event viewer to check for blue screen logs
        blue_screen_logs = subprocess.check_output(['wevtutil', 'q', 'System', '/c:1', '/f:xml', '/q:"*[System/EventID=41]"']).decode('utf-8')
        if blue_screen_logs:
            # Trigger self-heal if blue screen log is detected
            subprocess.Popen([sys.executable, SELF_HEAL_SCRIPT_PATH])
        time.sleep(300)

def manage_git_operations():
    while True:
        # Pull the latest changes from the git repository
        subprocess.run(['git', 'pull'], cwd=GIT_REPO_PATH)
        # Push any local changes to the git repository
        subprocess.run(['git', 'add', '-A'], cwd=GIT_REPO_PATH)
        subprocess.run(['git', 'commit', '-m', 'Auto commit'], cwd=GIT_REPO_PATH)
        subprocess.run(['git', 'push'], cwd=GIT_REPO_PATH)
        time.sleep(3600)

def execute_txf_risk_calculator():
    # Execute txf_risk_calculator.py with pre-configured parameters
    subprocess.Popen([sys.executable, TXF_RISK_CALCULATOR_PATH, 'param1', 'param2'])

def main():
    # Create threads for each task
    auto_start_thread = threading.Thread(target=auto_start_on_boot)
    memory_guardian_thread = threading.Thread(target=monitor_and_restart_memory_guardian)
    blue_screen_thread = threading.Thread(target=auto_detect_blue_screen_logs)
    git_thread = threading.Thread(target=manage_git_operations)
    txf_thread = threading.Thread(target=execute_txf_risk_calculator)

    # Start each thread
    auto_start_thread.start()
    memory_guardian_thread.start()
    blue_screen_thread.start()
    git_thread.start()
    txf_thread.start()

if __name__ == '__main__':
    main()
