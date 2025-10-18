from .speech_to_text import convert_speech_to_text
from .text_to_speech import speak_text
from .resume_generator import generate_resume

def start_voice_resume():
    print("\n🎙️ Welcome to the Voice-to-Resume Builder!\n")
    user_data = {}

    questions = {
        "name": "What is your full name?",
        "qualification": "What is your highest qualification?",
        "skills": "List your technical skills.",
        "experience": "Describe your work experience or projects.",
        "contact": "Provide your contact email or phone number."
    }

    for key, question in questions.items():
        speak_text(question)
        print(f"\n❓ {question}")
        answer = convert_speech_to_text()
        user_data[key] = answer
        print(f"✅ Recorded: {answer}")

    # Generate Resume
    generate_resume(user_data)
    print("\n📄 Resume generated successfully!")
