
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import datetime
from pathlib import Path

# Setup OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0)

# Define the domain/topic for the day (rotate over CISSP domains or load from list)
def get_daily_topic():
    topics = [
        "Security and Risk Management",
        "Asset Security",
        "Security Architecture and Engineering",
        "Communication and Network Security",
        "Identity and Access Management (IAM)",
        "Security Assessment and Testing",
        "Security Operations",
        "Software Development Security"
    ]
    day = datetime.datetime.now().weekday()
    return topics[day % len(topics)]

# Generate study notes and flashcards
def generate_study_content(topic):
    prompt = f"Summarize the CISSP domain: {topic}. Then generate 10 flashcards (Q&A format)."
    return chat.predict(prompt)

# Save output locally (can later upload to Notion)
def save_to_file(content, topic):
    today = datetime.date.today().isoformat()
    filename = f"CISSP_{topic.replace(' ', '_')}_{today}.txt"
    path = Path(filename)
    path.write_text(content)
    return str(path)

def main():
    topic = get_daily_topic()
    notes = generate_study_content(topic)
    filepath = save_to_file(notes, topic)
    print(f"Study content saved to: {filepath}")

if __name__ == "__main__":
    main()
