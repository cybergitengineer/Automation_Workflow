
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import requests
import smtplib
from email.mime.text import MIMEText

# Setup API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize ChatGPT model
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0)

# Scrape job postings (LinkedIn mock)
def scrape_jobs():
    # Replace with Apify or LinkedIn API
    return [
        {"title": "Cybersecurity Analyst", "company": "TechCorp", "url": "https://joblink1"},
        {"title": "AI Security Engineer", "company": "DataShield", "url": "https://joblink2"}
    ]

# Tailor resume for job
def tailor_resume(job):
    template = ChatPromptTemplate.from_template(
        "Tailor my resume to apply for a {title} role at {company}. Return as bullet points."
    )
    prompt = template.format(title=job['title'], company=job['company'])
    result = chat.predict(prompt)
    return result

# Email results
def send_email(summary):
    msg = MIMEText(summary, 'plain')
    msg['Subject'] = 'Daily Job Matches'
    msg['From'] = 'agenticmate@gmail.com'
    msg['To'] = 'agenticmate@gmail.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('agenticmate@gmail.com', os.getenv("EMAIL_PASSWORD"))
        server.send_message(msg)

def main():
    jobs = scrape_jobs()
    summaries = []
    for job in jobs:
        tailored = tailor_resume(job)
        summaries.append(f"Job: {job['title']} at {job['company']}
{tailored}
Link: {job['url']}
")
    send_email("\n".join(summaries))

if __name__ == "__main__":
    main()
