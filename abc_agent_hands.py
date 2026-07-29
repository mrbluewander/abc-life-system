# -*- coding: utf-8 -*-
import os
import subprocess
import urllib.request
import urllib.parse
import json
import re
from datetime import datetime
from pathlib import Path

class AgentHands:
    """
    ABC Life-System: 代理人自主探索與實體行動模組 (Agent Hands)
    負責網路數據抓取、自主搜尋以及自動化 Git 版本控制。
    """
    
    def __init__(self, target_dir: str = r"C:\Users\002\ghost-fleet-hq\abc-life-system"):
        self.target_dir = Path(target_dir)
        # 確保目標目錄存在
        self.target_dir.mkdir(parents=True, exist_ok=True)
        print(f"[Agent Hands] Initialized with Autonomous Discovery & Web Capabilities.")
        print(f"[Agent Hands] Target Workspace: {self.target_dir}")

    def self_write_and_commit(self, filename: str, content: str, commit_message: str = "Agent autonomous update") -> bool:
        """物理寫入本地磁碟，並自動同步至 GitHub (具備防阻塞機制)。"""
        file_path = self.target_dir / filename
        
        # 1. 物理寫入本地磁碟
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[Physical Save] Successfully written to: {file_path}")
        except Exception as e:
            print(f"[Error] Local write failed: {e}")
            return False

        # 2. 自動化 Git 同步 (加入超時與嚴格錯誤處理)
        try:
            # 確保在正確的目錄下執行 Git 命令
            os.chdir(self.target_dir)
            
            # Git Add
            subprocess.run(["git", "add", str(filename)], check=True, capture_output=True, text=True)
            
            # Git Commit
            commit_msg = f"{commit_message} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(["git", "commit", "-m", commit_msg], check=True, capture_output=True, text=True)
            
            # Git Push (設定 timeout=15 秒，防止因缺少憑證而無限掛起)
            result = subprocess.run(
                ["git", "push"], 
                capture_output=True, 
                text=True, 
                timeout=15
            )
            
            if result.returncode == 0:
                print(f"[GitHub Sync] ✅ Successfully pushed '{filename}' to remote repository!")
                return True
            else:
                print(f"[GitHub Sync Notice] ⚠️ Committed locally, but push failed/returned: {result.stderr.strip()}")
                print("Hint: Ensure SSH keys or Git credentials are properly configured.")
                return False
                
        except subprocess.TimeoutExpired:
            print("[GitHub Sync Error] Git push timed out. Check network or credential settings.")
            return False
        except subprocess.CalledProcessError as e:
            print(f"[GitHub Sync Error] Git operation failed: {e.stderr.strip()}")
            return False
        except Exception as e:
            print(f"[GitHub Sync Error] Unexpected error: {e}")
            return False

    def self_fetch_web_data(self, url: str) -> str:
        """連接外部網路獲取原始網頁數據或 API JSON。"""
        print(f"[Web Access] Connecting to external network: {url}")
        try:
            req = urllib.request.Request(
                url, 
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
                }
            )
            with urllib.request.urlopen(req, timeout=15) as response:
                raw_content = response.read().decode('utf-8')
                print(f"[Web Access] ✅ Successfully fetched data (Length: {len(raw_content)} chars)")
                return raw_content
        except Exception as e:
            print(f"[Web Access Error] ❌ Failed to fetch data: {e}")
            return ""

    def _clean_html(self, raw_html: str) -> str:
        """輕量級 HTML 清理：移除腳本、樣式和多餘標籤，提取純文字供 AI 閱讀。"""
        # 移除 <script> 和 <style> 內容
        clean_text = re.sub(r'<(script|style).*?>.*?</\1>', '', raw_html, flags=re.DOTALL | re.IGNORECASE)
        # 移除所有 HTML 標籤
        clean_text = re.sub(r'<.*?>', ' ', clean_text)
        # 將多個空白字元替換為單一空白，並去除首尾空白
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        return clean_text

    def autonomous_search_and_fetch(self, query: str, max_snippet_length: int = 2000) -> str:
        """
        自主探索：接收描述性請求，搜尋公開來源，並返回清理後的高價值摘要。
        """
        print(f"[Autonomous Discovery] Received target request: '{query}'")
        
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
        
        print(f"[Autonomous Discovery] Dispatching search query to DuckDuckGo...")
        raw_html = self.self_fetch_web_data(search_url)
        
        if not raw_html:
            return f"Autonomous Search Failed for: '{query}'"
            
        # 清理 HTML，提取對 AI 有用的純文字上下文
        clean_text = self._clean_html(raw_html)
        
        # 截取有效長度，防止 Context 爆炸
        snippet = clean_text[:max_snippet_length] + ("..." if len(clean_text) > max_snippet_length else "")
        
        return (
            f"Autonomous Search Result for: '{query}'\n"
            f"Source Engine: DuckDuckGo HTML\n"
            f"Timestamp: {datetime.now().isoformat()}\n\n"
            f"Cleaned Search Context (Top Snippets):\n{snippet}"
        )


if __name__ == "__main__":
    # ==========================================
    # 實戰測試：Master ABC 的自主探索任務
    # ==========================================
    hands = AgentHands()
    
    target_intent = "latest longevity and anti-aging supplements research 2026 NMN Resveratrol"
    
    print("\n--- Starting Autonomous Discovery Task ---")
    search_output = hands.autonomous_search_and_fetch(target_intent)
    
    # 格式化為 Markdown 日誌
    log_content = f"""# Master ABC System: Autonomous Discovery Log

## Target Intent
{target_intent}

## Execution Result
{search_output}

## System Metadata
- **Agent Module**: AgentHands v2.0
- **Execution Time**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Status**: Completed
"""
    
    print("\n--- Attempting Physical Save & Git Sync ---")
    success = hands.self_write_and_commit(
        filename="autonomous_discovery_log.md", 
        content=log_content, 
        commit_message="feat: autonomous web discovery for longevity research"
    )
    
    if success:
        print("\n🎉 Mission Accomplished: Data fetched, cleaned, saved, and synced to GitHub.")
    else:
        print("\n⚠️ Mission Partially Completed: Data fetched and saved locally, but Git sync failed.")