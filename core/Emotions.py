import random

MOODS = {
    "neutral": ["Okay.", "Understood."],
    "calm": ["Alright, take it easy.", "I'm here."],
    "alert": ["Pay attention.", "This needs care."]
}

current_mood = "neutral"

def respond_with_mood(text):
    prefix = random.choice(MOODS[current_mood])
    return f"{prefix} {text}"
