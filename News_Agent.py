
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import feedparser
from email.mime.text import MIMEText
import smtplib

# Setup OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.3)

# Fetch RSS feed
def fetch_news():
    feed_url = "https://feeds.arstechnica.com/arstechnica/technology-lab"
    feed = feedparser.parse(feed_url)
    top_items = feed.entries[:5]
    headlines = [f"{item.title} - {item.link}" for item in top_items]
    return "\n".join(headlines)

# Summarize news
def summarize_news(headlines):
    prompt = f"Summarize the following tech and cybersecurity headlines in 3–5 concise bullet points:\n{headlines}"
    return chat.predict(prompt)

# Email the summary
def send_email(summary):
    msg = MIMEText(summary, "plain")
    msg["Subject"] = "Daily Tech & Cyber News Summary"
    msg["From"] = "your_email@example.com"
    msg["To"] = "your_email@example.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your_email@example.com", os.getenv("EMAIL_PASSWORD"))
        server.send_message(msg)

def main():
    headlines = fetch_news()
    summary = summarize_news(headlines)
    send_email(summary)
    print("News summary sent!")

if __name__ == "__main__":
    main()
