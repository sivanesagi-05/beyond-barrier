import pyttsx3

def speak(text):
    """Speak the text aloud and wait until speaking finishes"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()  # blocking call ensures it finishes speaking
