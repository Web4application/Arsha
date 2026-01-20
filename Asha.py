from voice import listen, speak
from commands import handle_command

def main():
    speak("ASHA is online. I am listening.")

    while True:
        text = listen()
        if text:
            handle_command(text)

if __name__ == "__main__":
    main()
