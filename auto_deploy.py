#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABC Life-System: Automated Deployment & Verification Script
-----------------------------------------------------------
Purpose: Orchestrates the initialization, seeding, and health-check 
         of both Holographic Memory and Advanced Agentic JIT Memory Engines.
"""

import sys
import logging
from typing import Dict, Any

# --- 統一日誌配置 (與底層模組保持一致) ---
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [Deploy] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("ABC-Deploy")

# --- 種子數據配置 (集中管理，方便未來擴展或從 config.json 讀取) ---
SEED_DATA_HLME = [
    {
        "memory_id": "longevity_01",
        "category": "Longevity",
        "content": "Daily anti-aging knowledge base framework hosted on private channels.",
        "salience_score": 1.0
    },
    {
        "memory_id": "trading_01",
        "category": "Taiwan-Futures",
        "content": "1-minute and 3-minute K-line technical parameter monitoring routine.",
        "salience_score": 1.0
    }
]

SEED_DATA_JIT = [
    {
        "memory_id": "longevity_02",
        "category": "Longevity",
        "content": "Advanced anti-aging supplement synergy and protocol tracking.",
        "future_utility": 0.95,
        "factual_confidence": 1.0
    },
    {
        "memory_id": "trading_02",
        "category": "Taiwan-Futures",
        "content": "Real-time 1-min & 3-min K-line volatility management parameters.",
        "future_utility": 0.98,
        "factual_confidence": 1.0
    }
]

def main():
    logger.info("=" * 60)
    logger.info("   ABC Life-System: Auto-Deployment Sequence Initiated   ")
    logger.info("=" * 60)
    
    # ==========================================
    # 1. 初始化並驗證 Holographic Memory Engine (HLME)
    # ==========================================
    logger.info("[1/2] Initializing Holographic Memory Engine (HLME)...")
    try:
        from abc_holographic_memory import HolographicMemoryEngine
        
        holo_engine = HolographicMemoryEngine(owner="Master ABC")
        
        for seed in SEED_DATA_HLME:
            holo_engine.encode_and_store(
                memory_id=seed["memory_id"],
                category=seed["category"],
                content=seed["content"],
                salience_score=seed["salience_score"]
            )
            
        holo_res = holo_engine.physical_manifestation()
        
        # 安全訪問字典鍵，防止因 IOError 導致的 KeyError
        status = holo_res.get("status", "Unknown")
        total_nodes = holo_res.get("total_nodes", 0)
        
        if status == "Permanently Stored":
            logger.info(f"-> HLME Verification: ✅ SUCCESS ({total_nodes} nodes secured)")
        else:
            logger.warning(f"-> HLME Verification: ⚠️ WARNING ({status}) - {holo_res.get('message', 'No details')}")
            
    except ImportError as e:
        logger.error(f"-> HLME Verification: ❌ FAILED. Module not found. Error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"-> HLME Verification: ❌ FAILED. Unexpected error: {e}")
        sys.exit(1)

    # ==========================================
    # 2. 初始化並驗證 Advanced Agentic Memory Engine (JIT)
    # ==========================================
    logger.info("[2/2] Initializing Advanced Agentic Memory & JIT Engine...")
    try:
        from abc_advanced_agentic_memory import AdvancedAgenticMemoryEngine
        
        # 注意：如果您採用了上一輪優化建議將 jic_memorize 改名為 jit_memorize，請在此處同步修改
        agentic_engine = AdvancedAgenticMemoryEngine(owner="Master ABC")
        
        for seed in SEED_DATA_JIT:
            # 兼容處理：嘗試呼叫 jit_memorize，若無則退回 jic_memorize
            memorize_method = getattr(agentic_engine, "jit_memorize", getattr(agentic_engine, "jic_memorize", None))
            if not memorize_method:
                raise AttributeError("Neither 'jit_memorize' nor 'jic_memorize' found in AdvancedAgenticMemoryEngine")
                
            memorize_method(
                memory_id=seed["memory_id"],
                category=seed["category"],
                content=seed["content"],
                future_utility=seed["future_utility"],
                factual_confidence=seed["factual_confidence"]
            )
            
        agentic_res = agentic_engine.physical_manifestation()
        
        status = agentic_res.get("status", "Unknown")
        salient_nodes = agentic_res.get("salient_nodes", 0)
        
        if status == "Permanently Stored":
            logger.info(f"-> JIT Engine Verification: ✅ SUCCESS ({salient_nodes} salient nodes active)")
        else:
            logger.warning(f"-> JIT Engine Verification: ⚠️ WARNING ({status}) - {agentic_res.get('message', 'No details')}")
            
    except ImportError as e:
        logger.error(f"-> JIT Engine Verification: ❌ FAILED. Module not found. Error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"-> JIT Engine Verification: ❌ FAILED. Unexpected error: {e}")
        sys.exit(1)

    # ==========================================
    # 3. 部署完成總結
    # ==========================================
    logger.info("=" * 60)
    logger.info("   Auto-Deployment & Verification Completed Successfully! ")
    logger.info("   System is ready for Agent orchestration.              ")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()