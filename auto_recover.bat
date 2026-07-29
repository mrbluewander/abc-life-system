@echo off
chcp 65001 >nul
echo ========================================
echo   ABC Life-System 災後自動復原程序
echo ========================================
echo.

cd /d C:\Users\002\ghost-fleet-hq\abc-life-system

:: 1. 修復 Git 索引損壞
echo [1/5] 檢查 Git 狀態...
if exist .git\index (
    git status >nul 2>&1
    if errorlevel 1 (
        echo   - Git 索引損壞，正在修復...
        del /f /q .git\index
        git reset >nul 2>&1
        echo   - Git 已修復。
    ) else (
        echo   - Git 狀態正常。
    )
) else (
    echo   - Git 未初始化，正在重建...
    git init >nul 2>&1
    git add . >nul 2>&1
    git commit -m "Auto-recovery after BSOD" >nul 2>&1
    echo   - Git 已重建。
)

:: 2. 清理 Python 快取
echo [2/5] 清理 Python 快取...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
echo   - 快取已清理。

:: 3. 清理系統臨時檔案
echo [3/5] 清理系統臨時檔案...
del /f /q %TEMP%\*.tmp >nul 2>&1
del /f /q %TEMP%\*.log >nul 2>&1
echo   - 臨時檔案已清理。

:: 4. 同步 GitHub
echo [4/5] 同步 GitHub 倉庫...
git pull origin master >nul 2>&1
if errorlevel 1 (
    echo   - 同步失敗，嘗試強制拉取...
    git fetch --all >nul 2>&1
    git reset --hard origin/master >nul 2>&1
)
echo   - GitHub 同步完成。

:: 5. 檢查核心模組
echo [5/5] 檢查核心模組...
python -c "from agent_hands import AgentHands; print('   - AgentHands: OK')" 2>nul
if errorlevel 1 (
    echo   - AgentHands: 異常！
)
python -c "from abc_holographic_memory import HolographicMemoryEngine; print('   - Memory Engine: OK')" 2>nul
if errorlevel 1 (
    echo   - Memory Engine: 異常！
)

echo.
echo ========================================
echo   復原完成！系統已就緒。
echo ========================================
echo.
pause