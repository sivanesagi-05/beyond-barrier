from voice_to_resume.workflow import start_voice_resume
from voice_to_resume.resume_generator import generate_resume

if __name__ == "__main__":
    print("🎙️ Voice to Resume Project Started")

    # Collect user responses via voice
    user_data = start_voice_resume()

    # Generate Word resume from captured data
    generate_resume()
