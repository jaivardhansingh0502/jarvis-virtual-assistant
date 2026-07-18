import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)   # Zira

for text in ["Hello", "How are you?", "Testing"]:
    engine.say(text)
    engine.runAndWait()