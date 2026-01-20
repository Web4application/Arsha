import speech_recognition as sr
import pyttsx3
from config import VOICE_RATE

engine = pyttsx3.init()
engine.setProperty("rate", VOICE_RATE)

def speak(text):
    print("ASHA:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source)

    try:
        return r.recognize_google(audio).lower()
    except:
        return ""
