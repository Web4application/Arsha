def detect_intent(text):
    if any(x in text for x in ["open", "create", "delete", "read"]):
        return "system"

    if any(x in text for x in ["remember", "forget", "recall"]):
        return "memory"

    if any(x in text for x in ["how are you", "feel", "mood"]):
        return "emotion"

    return "chat"
