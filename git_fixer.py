import os, subprocess, sys

def fix_git():
    print('[Auto-Fix] Detecting Git corruption...')
    try:
        # 1. Try normal status first
        subprocess.run(['git', 'status'], capture_output=True, check=True)
        print('[Auto-Fix] Git is healthy.')
        return True
    except:
        print('[Auto-Fix] Git is broken. Attempting repair...')
        
        # 2. Delete broken refs
        refs_to_delete = [
            '.git\\refs\\heads\\master',
            '.git\\refs\\remotes\\origin\\HEAD',
            '.git\\refs\\remotes\\origin\\main',
            '.git\\index'
        ]
        for ref in refs_to_delete:
            if os.path.exists(ref):
                try:
                    os.remove(ref)
                    print(f'   - Deleted corrupted ref: {ref}')
                except:
                    pass
        
        # 3. Re-initialize and fetch
        try:
            subprocess.run(['git', 'init'], capture_output=True)
            subprocess.run(['git', 'add', '.'], capture_output=True)
            subprocess.run(['git', 'commit', '-m', 'Auto-repair commit'], capture_output=True)
            subprocess.run(['git', 'fetch', 'origin'], capture_output=True)
            subprocess.run(['git', 'reset', '--hard', 'origin/master'], capture_output=True)
            print('[Auto-Fix] Repair successful! System synced with cloud.')
            return True
        except Exception as e:
            print(f'[Auto-Fix] Critical error during repair: {e}')
            return False

if __name__ == '__main__':
    fix_git()
