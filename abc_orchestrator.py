
import subprocess
import sys
import os
import shutil
import time
import git

class HarnessCore:
    def __init__(self):
        pass

    def protect(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error occurred: {e}")
        return wrapper

def main():
    harness = HarnessCore()

    @harness.protect
    def start_memory_guardian():
        try:
            subprocess.Popen(['python', 'memory_guardian.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        except Exception:
            pass

    @harness.protect
    def txfriskcalc():
        print("TXF Risk Calc")
        # Add your TXF Risk Calc logic here
        time.sleep(2)

    @harness.protect
    def youtubeassimilation():
        print("YouTube Assimilation")
        # Add your YouTube Assimilation logic here
        time.sleep(2)

    @harness.protect
    def systemhealthcheck():
        print("System Health Check")
        # Add your System Health Check logic here
        time.sleep(2)

    @harness.protect
    def auto_git_commit():
        try:
            repo = git.Repo()
            repo.git.add(all=True)
            repo.git.commit('-m', 'Auto commit after task')
        except Exception as e:
            print(f"Error occurred during auto git commit: {e}")

    while True:
        print("\nMenu:")
        print("1. TXF Risk Calc")
        print("2. YouTube Assimilation")
        print("3. System Health Check")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            start_memory_guardian()
            txfriskcalc()
            auto_git_commit()
        elif choice == '2':
            start_memory_guardian()
            youtubeassimilation()
            auto_git_commit()
        elif choice == '3':
            start_memory_guardian()
            systemhealthcheck()
            auto_git_commit()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
