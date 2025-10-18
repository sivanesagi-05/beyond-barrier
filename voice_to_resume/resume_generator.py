from docx import Document

def generate_resume(data):
    doc = Document()
    doc.add_heading("Resume", 0)

    doc.add_paragraph(f"Name: {data.get('name', '')}")
    doc.add_paragraph(f"Qualification: {data.get('qualification', '')}")
    doc.add_paragraph(f"Skills: {data.get('skills', '')}")
    doc.add_paragraph(f"Experience: {data.get('experience', '')}")
    doc.add_paragraph(f"Contact: {data.get('contact', '')}")

    doc.save("generated_resume.docx")
