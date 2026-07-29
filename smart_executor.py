from multi_brain_router import router
import subprocess, sys

def smart_execute(code_str):
    try:
        exec(code_str)
        print("✅ Execution successful!")
    except Exception as e:
        print(f"❌ Error detected: {e}")
        print("🔄 Attempting self-healing...")
        fixed_code = router.self_heal_code(code_str, str(e))
        # Clean up markdown fences if present
        clean_code = fixed_code.replace("```python", "").replace("```", "").strip()
        print(f"✨ Fixed Code:\n{clean_code}")
        try:
            exec(clean_code)
            print("✅ Self-healed execution successful!")
        except Exception as e2:
            print(f"❌ Second attempt failed: {e2}")

# Test it
smart_execute("print("Hello Master ABC")")
smart_execute("print("Missing bracket"")