#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABC Life-System: Holographic Layered Memory Engine (HLME)
---------------------------------------------------------
Inspired by State-of-the-Art Agent Memory Architectures (2026 A-MEM & Temporal Graph Memory):
  1. Atomic Zettelkasten Memory Nodes: Prevents memory homogenization and overlaps.
  2. Dynamic Graph Linkage: Connects cross-session insights (Longevity, Trading, Routines).
  3. Temporal Encoding Gate: Filters noise, retains high-salience facts, eliminates amnesia.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# --- 企業級日誌配置 ---
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [HLME] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("ABC-HLME")

class HolographicMemoryEngine:
    """
    全息分層記憶引擎 (HLME)。
    提供原子化記憶儲存、時間序列索引與基礎圖譜連結能力。
    """
    
    def __init__(self, owner: str = "Master ABC", db_path: str = "abc_holographic_memory.json"):
        self.owner = owner
        self.db_path = Path(db_path)
        
        # 核心數據結構
        self.memory_nodes: Dict[str, Dict[str, Any]] = {}
        self.temporal_index: List[str] = []  # 維持時間順序的 ID 列表
        
        # 啟動時自動恢復記憶狀態 (Frictionless Persistence)
        self._load_from_disk()
        logger.info(f"[{self.owner}] Holographic Layered Memory initialized.")

    def encode_and_store(self, memory_id: str, category: str, content: str, 
                         salience_score: float = 1.0, linked_ids: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        編碼並儲存原子化記憶節點 (Atomic Zettelkasten)。
        包含防重疊機制與基礎圖譜連結 (Dynamic Graph Linkage) 支援。
        """
        # 1. 防重疊/更新機制：若 ID 已存在，先從時間索引中移除舊位置
        if memory_id in self.memory_nodes:
            logger.warning(f"Node '{memory_id}' already exists. Updating content and refreshing temporal position.")
            if memory_id in self.temporal_index:
                self.temporal_index.remove(memory_id)
        
        # 2. 建構全息節點
        node = {
            "id": memory_id,
            "category": category,
            "content": content,
            "salience_score": float(salience_score),
            "timestamp": datetime.now().isoformat(),
            "linked_ids": linked_ids or []  # 為未來的動態圖譜連結預留介面
        }
        
        # 3. 寫入記憶體與時間索引
        self.memory_nodes[memory_id] = node
        self.temporal_index.append(memory_id)  # 附加到末尾，代表最新時間戳
        
        logger.info(f"Encoded atomic node '{memory_id}' under [{category}] with salience {salience_score:.2f}")
        
        # 4. 自動觸發實體化，確保零遺失
        self.physical_manifestation()
        return node

    def retrieve_context(self, category: Optional[str] = None, top_k: int = 10) -> List[Dict[str, Any]]:
        """
        檢索上下文 (Temporal Encoding Gate)。
        根據顯著性分數與時間新舊度進行智能排序，並限制返回數量以防止 Token 爆滿。
        """
        nodes = list(self.memory_nodes.values())
        
        # 1. 類別過濾
        if category:
            nodes = [n for n in nodes if n['category'] == category]
            
        # 2. 時間編碼閘道排序：優先按 salience_score (降序)，其次按 timestamp (降序，最新的在前)
        nodes.sort(key=lambda x: (x['salience_score'], x['timestamp']), reverse=True)
        
        # 3. 截取 Top-K，實現 Token 經濟
        retrieved_nodes = nodes[:top_k]
        
        logger.info(f"Retrieved {len(retrieved_nodes)} nodes for category: {category or 'All'} (Top {top_k})")
        return retrieved_nodes

    def physical_manifestation(self) -> Dict[str, Any]:
        """
        實體化：將全息記憶與時間索引永久寫入本地硬碟。
        """
        try:
            payload = {
                "memory_nodes": self.memory_nodes,
                "temporal_index": self.temporal_index,
                "last_updated": datetime.now().isoformat()
            }
            
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump(payload, f, indent=2, ensure_ascii=False)
                
            logger.info(f"Manifested to disk: {self.db_path} | Nodes: {len(self.memory_nodes)}")
            
            return {
                "file": str(self.db_path), 
                "status": "Permanently Stored", 
                "total_nodes": len(self.memory_nodes)
            }
        except IOError as e:
            logger.error(f"Failed to manifest memory to disk: {e}")
            return {"status": "Error", "message": str(e)}

    def _load_from_disk(self):
        """內部方法：啟動時從本地硬碟恢復全息記憶狀態"""
        if self.db_path.exists():
            try:
                with open(self.db_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.memory_nodes = data.get("memory_nodes", {})
                    self.temporal_index = data.get("temporal_index", [])
                logger.info(f"Memory successfully restored from {self.db_path}.")
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load memory file. Starting fresh. Error: {e}")
                self.memory_nodes = {}
                self.temporal_index = []


if __name__ == "__main__":
    # ==========================================
    # 實戰測試：Master ABC 的全息記憶初始化 (V1 基礎版)
    # ==========================================
    engine = HolographicMemoryEngine(owner="Master ABC")
    
    # 1. 編碼長壽/健康模組 (V1)
    engine.encode_and_store(
        memory_id="longevity_01", 
        category="Longevity", 
        content="Daily anti-aging knowledge base framework hosted on private channels.",
        salience_score=0.9
    )
    
    # 2. 編碼高頻交易模組 (V1)
    engine.encode_and_store(
        memory_id="trading_01", 
        category="Taiwan-Futures", 
        content="1-minute and 3-minute K-line technical parameter monitoring routine.",
        salience_score=0.95,
        linked_ids=["longevity_01"]  # 示範：建立跨領域的基礎圖譜連結 (例如：健康狀態影響交易心態)
    )
    
    # 3. 測試重複編碼 (防重疊機制)
    engine.encode_and_store(
        memory_id="trading_01", 
        category="Taiwan-Futures", 
        content="UPDATED: 1-min, 3-min, AND 15-min K-line volatility monitoring routine.",
        salience_score=0.98
    )
    
    # 4. 編譯並查看 AI 視角下的「全息上下文」
    print("\n--- 檢索 Taiwan-Futures 領域上下文 (Top 5) ---")
    trading_ctx = engine.retrieve_context(category="Taiwan-Futures", top_k=5)
    for item in trading_ctx:
        print(f"[Score: {item['salience_score']}] [Linked: {item['linked_ids']}] {item['content']}")
        
    print("\n--- 檢索全域上下文 (Top 3) ---")
    all_ctx = engine.retrieve_context(top_k=3)
    for item in all_ctx:
        print(f"[{item['category']}] [Score: {item['salience_score']}] {item['content']}")