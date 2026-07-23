import ollama

from config import OLLAMA_MODEL
from src.prompts import PRIVACY_POLICY_PROMPT


def analyze_with_ai(text):
    prompt = f"{PRIVACY_POLICY_PROMPT}\n\n{text}"

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]