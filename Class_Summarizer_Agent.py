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


# Setup OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.2)

# Read transcript or class notes from file
def load_class_notes(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Summarize notes
def summarize_class(notes):
    prompt = f"Summarize the following university lecture transcript into key points with bullet list and 3 takeaway questions:\n{notes}"
    return chat.invoke(prompt)

# Save output
from langchain_core.messages import AIMessage  # Add this if not already imported

# Save output to file
def save_summary(summary):
    if isinstance(summary, AIMessage):
        summary = summary.content

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    path = output_dir / f"Class_Summary_{timestamp}.txt"
    path.write_text(summary, encoding="utf-8")
    return str(path)



def main():
    # Replace with your actual transcript file path
    transcript_file = "class_transcript.txt"
    if not os.path.exists(transcript_file):
        print(f"Transcript file '{transcript_file}' not found.")
        return
    notes = load_class_notes(transcript_file)
    summary = summarize_class(notes)
    output_path = save_summary(summary)
    print(f"Class summary saved to: {output_path}")

if __name__ == "__main__":
    main()
