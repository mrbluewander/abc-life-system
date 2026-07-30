import psutil, time, os

def memory_guardian(limit_percent=85):
    while True:
        mem = psutil.virtual_memory()
        if mem.percent > limit_percent:
            print(f'⚠️ Memory Critical: {mem.percent}%! Killing non-essential processes...')
            # 這裡可以加入自動關閉非必要程式的邏輯
            # 例如：os.system('taskkill /F /IM chrome.exe') 
            time.sleep(60) # 冷卻一分鐘再檢查
        else:
            time.sleep(10) # 正常狀態每10秒檢查一次

if __name__ == '__main__':
    print('️ Memory Guardian Activated. Limit: 85%')
    memory_guardian()
