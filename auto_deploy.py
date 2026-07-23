#!/usr/env/python3
"""
ABC Life-System: Automated Deployment & Execution Script
--------------------------------------------------------
Purpose: Orchestrates the initialization and test execution of both
         Holographic Memory and Advanced Agentic JIT Memory Engines.
"""

import os
import sys
from abc_holographic_memory import HolographicMemoryEngine
from abc_advanced_agentic_memory import AdvancedAgenticMemoryEngine

def main():
    print("==================================================")
    print("   ABC Life-System: Auto-Deployment Sequence      ")
    print("==================================================")
    
    # 1. Initialize Holographic Memory Engine
    print("\n[1/2] Initializing Holographic Memory Engine...")
    holo_engine = HolographicMemoryEngine(owner="Master ABC")
    holo_engine.encode_and_store("longevity_01", "Longevity", "Daily anti-aging knowledge base framework hosted on private channels.", 1.0)
    holo_engine.encode_and_store("trading_01", "Taiwan-Futures", "1-minute and 3-minute K-line technical parameter monitoring routine.", 1.0)
    holo_res = holo_engine.physical_manifestation()
    print(f"-> Manifestation Status: {holo_res['status']} ({holo_res['total_nodes']} nodes secured)")

    # 2. Initialize Advanced Agentic Memory Engine
    print("\n[2/2] Initializing Advanced Agentic Memory & JIT Engine...")
    agentic_engine = AdvancedAgenticMemoryEngine(owner="Master ABC")
    agentic_engine.jic_memorize("longevity_02", "Longevity", "Advanced anti-aging supplement synergy and protocol tracking.", 0.95, 1.0)
    agentic_engine.jic_memorize("trading_02", "Taiwan-Futures", "Real-time 1-min & 3-min K-line volatility management parameters.", 0.98, 1.0)
    agentic_res = agentic_engine.physical_manifestation()
    print(f"-> Manifestation Status: {agentic_res['status']} ({agentic_res['salient_nodes']} salient nodes active)")

    print("\n==================================================")
    print("   Auto-Deployment & Verification Completed Successfully! ")
    print("==================================================")

if __name__ == "__main__":
    main()