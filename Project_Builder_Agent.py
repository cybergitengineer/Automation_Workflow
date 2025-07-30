
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pathlib import Path
import datetime

# Setup OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.4)

# Define today's project prompt (user can change this)
def get_project_idea():
    return "Build a simple AI-powered vulnerability scanner using Python and Nmap."

# Generate project scaffold/instructions
def generate_project_plan(idea):
    prompt = f"Generate a GitHub-ready README and initial project plan for the following idea: {idea}. Include:
- Project description
- Installation steps
- File structure
- Sample code for main.py
- Example usage"
    return chat.predict(prompt)

# Save output
def save_output(plan, idea):
    today = datetime.date.today().isoformat()
    filename = f"Project_Scaffold_{today}.md"
    Path(filename).write_text(plan)
    return filename

def main():
    idea = get_project_idea()
    plan = generate_project_plan(idea)
    path = save_output(plan, idea)
    print(f"Project plan saved to: {path}")

if __name__ == "__main__":
    main()
