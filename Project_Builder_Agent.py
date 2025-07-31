from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate  # Only needed if you're using prompts
import datetime
from pathlib import Path

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize chat model
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.2)


# Setup OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.4)

# Define today's project prompt (user can change this)
def get_project_idea():
    return "Build a simple AI-powered vulnerability scanner using Python and Nmap."

# Generate project scaffold/instructions
def generate_project_plan(idea):
    prompt = f"""Generate a GitHub-ready README and initial project plan for the following idea: {idea}. Include:
- Project description
- Installation steps
- File structure
- Sample code for main.py
- Example usage"""
    return chat.invoke(prompt)


# Save output
def save_output(plan, idea):
    # Convert AIMessage to plain string
    if hasattr(plan, "content"):
        plan = plan.content

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    filename = f"Project_Scaffold_{timestamp}.md"
    path = output_dir / filename
    path.write_text(plan, encoding="utf-8")
    return path


def main():
    idea = get_project_idea()
    plan = generate_project_plan(idea)
    path = save_output(plan, idea)
    print(f"Project plan saved to: {path}")

if __name__ == "__main__":
    main()
