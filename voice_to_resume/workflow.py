from voice_to_resume.speech_to_text import get_audio_input
from voice_to_resume.text_to_speech import speak
from voice_to_resume.utils import save_to_json

def ask_question(question):
    """Speak question + print, then capture voice input"""
    speak(question)          # Speak aloud
    print(f"\n❓ {question}")  # Print for reference

    answer = get_audio_input()  # Listen until user stops
    if not answer:
        answer = "No response captured"
    return answer

def start_voice_resume():
    speak("Welcome to the Voice-Based Resume Builder!")
    print("\n🧠 Voice-Based Resume Builder\n")

    questions = [
        "What is your name?",
        "What is your current qualification?",
        "What are your technical skills?",
        "What projects have you worked on?",
        "What is your career objective?"
    ]

    user_data = {}
    for q in questions:
        user_data[q] = ask_question(q)

    print("\n✅ Data Collected:")
    for key, value in user_data.items():
        print(f"{key}: {value}")

    save_to_json(user_data)
    return user_data
