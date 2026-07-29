@echo off  
chcp 65001 >nul  
echo ========================================  
  ABC Life-System 極限自動復原程序 v3  
  
cd /d C:\Users\002\ghost-fleet-hq\abc-life-system  
  
[1/4] 執行 Git 深度修復...  
python git_fixer.py  
  
[2/4] 清理快取...  
for /d /r . %%%%d in (__pycache__) do @if exist "%%%%d" rd /s /q "%%%%d"  
  
[3/4] 驗證核心模組...  
python -c "from agent_hands import AgentHands; print('   - AgentHands: OK')"  
  
[4/4] 同步雲端...  
git pull origin master --rebase  
  
========================================  
  復原完成！  
