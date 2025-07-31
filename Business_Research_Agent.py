from dotenv import load_dotenv
import os
from pathlib import Path
import datetime
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize ChatOpenAI
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.2)

# Setup OpenAI model
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.3)

# Define the business idea for the day (can cycle or be input manually)
def get_business_idea():
    return "AI-powered telehealth platform for Zambia"

# Generate market research
def generate_market_research(idea):
    prompt = f"Create a market analysis for this idea: {idea}. Include market size, key competitors, customer segments, and opportunities in 500 words."
    return chat.invoke(prompt)

# Generate financial model summary
def generate_financial_model(idea):
    prompt = f"Generate a basic revenue projection for a startup based on the idea: {idea}. Assume conservative, moderate, and optimistic scenarios."
    return chat.predict(prompt)

# Save both outputs to a text file
def save_to_file(content, topic):
    # Extract actual string content from AIMessage
    if hasattr(content, "content"):
        content = content.content

    # Use a timestamp for uniqueness
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"CISSP_{topic.replace(' ', '_')}_{timestamp}.txt"

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    path = output_dir / filename
    path.write_text(content, encoding="utf-8")
    return str(path)



def main():
    idea = get_business_idea()
    research = generate_market_research(idea)
    finance = generate_financial_model(idea)
    filepath = save_outputs(research, finance, idea)
    print(f"Research saved to: {filepath}")

if __name__ == "__main__":
    main()
