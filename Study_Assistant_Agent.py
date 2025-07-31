from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate  # Only if needed
import datetime
from pathlib import Path

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize ChatOpenAI
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.2)



# Setup OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


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
    return chat.invoke(prompt)

# Save output locally (can later upload to Notion)
from pathlib import Path
import datetime

def save_to_file(content, topic):
    from langchain_core.messages import AIMessage  # Only if not already imported

    # Ensure we save just the string content
    if isinstance(content, AIMessage):
        content = content.content

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"CISSP_{topic.replace(' ', '_')}_{timestamp}.txt"

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    path = output_dir / filename
    path.write_text(content, encoding="utf-8")
    return str(path)


def main():
    topic = get_daily_topic()
    notes = generate_study_content(topic)
    filepath = save_to_file(notes, topic)
    print(f"Study content saved to: {filepath}")

if __name__ == "__main__":
    main()
