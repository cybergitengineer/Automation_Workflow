
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pathlib import Path
import datetime

# Setup OpenAI model
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.3)

# Define the business idea for the day (can cycle or be input manually)
def get_business_idea():
    return "AI-powered telehealth platform for Zambia"

# Generate market research
def generate_market_research(idea):
    prompt = f"Create a market analysis for this idea: {idea}. Include market size, key competitors, customer segments, and opportunities in 500 words."
    return chat.predict(prompt)

# Generate financial model summary
def generate_financial_model(idea):
    prompt = f"Generate a basic revenue projection for a startup based on the idea: {idea}. Assume conservative, moderate, and optimistic scenarios."
    return chat.predict(prompt)

# Save both outputs to a text file
def save_outputs(research, finance, idea):
    today = datetime.date.today().isoformat()
    filename = f"Business_Idea_Research_{today}.txt"
    content = f"Business Idea: {idea}

--- Market Research ---
{research}

--- Financial Model ---
{finance}"
    path = Path(filename)
    path.write_text(content)
    return str(path)

def main():
    idea = get_business_idea()
    research = generate_market_research(idea)
    finance = generate_financial_model(idea)
    filepath = save_outputs(research, finance, idea)
    print(f"Research saved to: {filepath}")

if __name__ == "__main__":
    main()
