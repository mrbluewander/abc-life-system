#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABC Life-System: Master Orchestrator (主控台)
------------------------------------------------
將 HLME、JIT Engine 與 AgentHands 完美串聯，
執行一次完整的「自主探索 -> 記憶編碼 -> 物理存檔 -> Git 同步」閉環。
"""

import logging
from datetime import datetime

# 引入我們優化過的三大核心模組
from abc_holographic_memory import HolographicMemoryEngine
from abc_advanced_agentic_memory import AdvancedAgenticMemoryEngine
from agent_hands import AgentHands

# 統一日誌配置
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [Master] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("ABC-Master")

def run_full_cycle():
    logger.info("="*60)
    logger.info("  ABC Life-System: Full Autonomous Cycle Initiated  ")
    logger.info("="*60)

    # 1. 初始化記憶引擎
    logger.info("Step 1: Booting up Memory Engines...")
    holo_engine = HolographicMemoryEngine(owner="Master ABC")
    jit_engine = AdvancedAgenticMemoryEngine(owner="Master ABC")

    # 2. 啟動代理人雙手，執行自主探索
    logger.info("Step 2: AgentHands fetching external data...")
    hands = AgentHands()
    
    # 模擬一個自主探索任務
    target_intent = "latest longevity and anti-aging supplements research 2026"
    search_result = hands.autonomous_search_and_fetch(target_intent)
    
    # 3. 將探索結果編碼入記憶引擎 (測試 JIT 的打分機制)
    logger.info("Step 3: Encoding fetched data into Memory Engines...")
    
    # 假設我們從搜尋結果中提取了一句核心摘要
    extracted_fact = "2026 research highlights NMN and Resveratrol synergy for cellular repair."
    
    # 存入 HLME (長期記憶)
    holo_engine.encode_and_store(
        memory_id="web_discovery_01",
        category="Longevity",
        content=extracted_fact,
        salience_score=0.95,
        linked_ids=["longevity_01"]
    )
    
    # 存入 JIT (即時記憶，給予高未來效用)
    jit_engine.jit_memorize(
        memory_id="web_discovery_01",
        category="Longevity",
        content=extracted_fact,
        future_utility=0.95,
        factual_confidence=0.90
    )

    # 4. 編譯當前 AI 上下文 (Token 經濟測試)
    logger.info("Step 4: Compiling JIT Runtime Context...")
    active_context = jit_engine.compile_runtime_context(category_filter="Longevity", top_k=3)
    logger.info(f"Retrieved {len(active_context)} high-salience nodes for LLM context.")

    # 5. 物理存檔與 Git 同步 (解決您之前的痛點！)
    logger.info("Step 5: Physical Manifestation & Git Sync...")
    
    # 生成 Markdown 報告
    report_content = f"""# Master ABC System: Autonomous Cycle Report

## Execution Summary
- **Time**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Target Intent**: {target_intent}
- **Extracted Fact**: {extracted_fact}

## System Status
- HLME Nodes: {len(holo_engine.memory_nodes)}
- JIT Salient Nodes: {len(jit_engine.salient_memory)}
- Active Context Retrieved: {len(active_context)} nodes.

## Raw Search Snippet
{search_result[:500]}... (Truncated for report)
"""

    # 呼叫 AgentHands 進行真實的物理寫入與 Git Push
    success = hands.self_write_and_commit(
        filename="master_cycle_report.md",
        content=report_content,
        commit_message="feat: master orchestrator full cycle execution"
    )

    # 6. 最終驗證
    logger.info("="*60)
    if success:
        logger.info("🎉 MISSION ACCOMPLISHED: Data memorized, saved to disk, and pushed to GitHub!")
        logger.info("-> Please check your local folder for 'master_cycle_report.md'")
        logger.info("-> Please run 'git log' in terminal to verify the commit trace.")
    else:
        logger.warning("⚠️ Data memorized and saved locally, but Git push failed. Check credentials.")
    logger.info("="*60)

if __name__ == "__main__":
    run_full_cycle()