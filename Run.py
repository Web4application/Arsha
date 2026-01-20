from core.voice import listen, speak
from core.brain import ask_ai
from core.intents import detect_intent
from tools.web import web_search

def main():
    speak("ASHA is online. How can I help you?")

    while True:
        text = listen()
        if not text:
            continue

        if "stop" in text or "exit" in text:
            speak("Goodbye.")
            break

        intent = detect_intent(text)

        if intent == "web":
            result = web_search(text)
            speak(result)

        else:
            reply = ask_ai(text)
            speak(reply)

if __name__ == "__main__":
    main()
