from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI  # ✅ Correct import
from langchain.prompts import ChatPromptTemplate
import requests
import smtplib
from email.mime.text import MIMEText

# Load .env values
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI chat model
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.2)

# prompt = "List the top 5 cybersecurity job openings today with company names and required skills."
from langchain.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template("Find a job in {field}")
prompt = prompt_template.format_messages(field="cybersecurity")
listings = chat.invoke(prompt)
print(listings.content)

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize ChatOpenAI
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.2)

# Save job listings to a text file
from pathlib import Path
import datetime
from langchain_core.messages import AIMessage

def save_job_listings(listings):
    if hasattr(listings, "content"):  # handle AIMessage or similar
        listings = listings.content

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    filename = output_dir / f"Job_Hunter_Results_{timestamp}.txt"
    content = f"""Job Listings - {timestamp}

{listings}
"""
    filename.write_text(content, encoding="utf-8")
    return str(filename)

output_path = save_job_listings(listings)
print(f"File saved at: {output_path}")



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
    return chat.invoke(prompt)

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
        summaries.append(f"""Job: {job['title']} at {job['company']}
{tailored}
Link: {job['url']}""")

    send_email("\n".join(summaries))

if __name__ == "__main__":
    main()
