import sounddevice as sd
import wavio
import speech_recognition as sr

def record_voice(filename="response.wav", duration=5, fs=44100):
    print("🎙️ Recording... please speak now.")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    wavio.write(filename, audio, fs, sampwidth=2)
    print(f"✅ Audio saved as {filename}")

def convert_speech_to_text(filename="response.wav"):
    record_voice(filename)
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio."
