import os 
from dotenv import load_dotenv
from groq import Groq 
from pypdf import PdfReader



load_dotenv()
my_api_key= os.getenv("GROQ_API_KEY")
reader= PdfReader("Arjun_NewResume.pdf")
resume_text=reader.pages[0].extract_text()
hr_resume_keywords = [
    # Programming Languages
    "Python", "JavaScript", "Java", "C++", "SQL", 
    
    # Frameworks & Libraries
    "React", "Django", "FastAPI", "Pandas", "Node.js", 
    
    # Tools & Cloud
    "Git", "Docker", "AWS", "Kubernetes", 
    
    # Soft Skills & Methodologies
    "Agile", "Scrum", "Team Leadership", "Problem Solving"
]
response_format={
    "type":"json_object",
}
client= Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"
system_message={
    "role":"system",
    "content": "You are a resume parser. You will be given a resume in text format. Your task is to extract relevant information from the resume and return it in a structured JSON format. The JSON should include the following fields: name, email, phone, education, experience, skills, and any other relevant information you can extract. If any field is not present in the resume, return an empty string for that field."
}
message={
    "role":"user",
    "content": f"Extract relevant information from the following resume text: {resume_text}. The resume should be parsed based on the following HR keywords: {', '.join(hr_resume_keywords)}. Please return the extracted in the form of match percentage for each keyword and the overall match percentage. The output should be in JSON format but dont reurn the whole resume text just the percentage of match for each keyword and the overall match percentage."
}
messages=[system_message,message]
response=client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1,
    response_format=response_format

)
print(response.choices[0].message.content)
