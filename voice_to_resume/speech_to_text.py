import speech_recognition as sr

def get_audio_input():
    """Capture user voice input until user stops speaking naturally"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        # Listen until user stops speaking naturally
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand audio.")
        return None
    except sr.RequestError:
        print("❌ Speech Recognition service unavailable.")
        return None
