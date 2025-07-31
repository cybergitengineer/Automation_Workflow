from dotenv import load_dotenv
import os
import feedparser
from email.mime.text import MIMEText
import smtplib

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Updated LangChain import (fixes deprecation warning)
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


# Setup OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.3)

# Save news summary to a text file
def save_news_summary(summary):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    filename = f"News_Digest_{timestamp}.txt"
    content = f"""Daily News Summary - {timestamp}

{summary}
"""

    path = output_dir / filename
    path.write_text(content, encoding="utf-8")
    return str(path)

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
    return chat.invoke(prompt)

# Email the summary
def send_email(summary):
    if hasattr(summary, "content"):
        summary = summary.content
    msg = MIMEText(summary)
    msg["Subject"] = "Daily Tech News Summary"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("EMAIL_USER")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD"))
        server.send_message(msg)

def main():
    headlines = fetch_news()
    summary = summarize_news(headlines)
    send_email(summary)
    print("News summary sent!")

if __name__ == "__main__":
    main()
