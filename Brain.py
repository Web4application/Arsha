import requests
from config import OPENAI_API_KEY

def think(prompt):
    r = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4.1-mini",
            "messages": [
                {"role": "system", "content": "You are ASHA, a disciplined personal AI."},
                {"role": "user", "content": prompt}
            ]
        }
    )
    return r.json()["choices"][0]["message"]["content"]
