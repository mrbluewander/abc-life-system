import os, subprocess
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

class MultiBrainRouter:
    def __init__(self):
        self.groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    def think(self, prompt, model="groq"):
        if model == "groq":
            chat = self.groq_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile"
            )
            return chat.choices[0].message.content
        return "Model not supported"

    def self_heal_code(self, broken_code, error_msg):
        prompt = f"The following Python code failed with error: {error_msg}. Please fix the code and output ONLY the corrected code:\n{broken_code}"
        return self.think(prompt)

router = MultiBrainRouter()
print("✅ Self-healing router initialized!")