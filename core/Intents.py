def detect_intent(text):
    if any(x in text for x in ["open", "create", "delete", "read"]):
        return "files"

    if any(x in text for x in ["search", "look up", "find info"]):
        return "web"

    return "chat"
