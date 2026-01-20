git remote add origin git@github.com:Web4application/Arsha.git
git branch -M main
git push -u origin main
pip install SpeechRecognition pyttsx3 pyaudio
pip install pipwin
pipwin install pyaudio
brew install portaudio
pip install pyaudio
sudo apt install portaudio19-dev
pip install pyaudio
# folder
asha/
├── asha.py          # main brain
├── memory.json      # local memory
├── commands.py      # command logic
└── voice.py         # speech in/out

# offline architecture
asha/
├── core/
│   ├── asha.py              # main loop
│   ├── voice.py             # speech in/out
│   ├── brain.py             # reasoning & intent
│   ├── emotions.py          # mood + tone
│
├── system/
│   ├── files.py             # file & folder control
│   ├── apps.py              # open apps
│   ├── security.py          # command safety
│
├── memory/
│   ├── memory.json          # short-term memory
│   ├── longterm.db          # long-term memory (SQLite)
│
├── ai/
│   ├── local_llm.py         # offline AI brain (later)
│
├── ui/
│   ├── tray.py              # system tray
│
└── run.py                   # start ASHA
