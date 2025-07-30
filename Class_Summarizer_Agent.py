
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pathlib import Path
import datetime

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
    return chat.predict(prompt)

# Save output
def save_summary(summary):
    today = datetime.date.today().isoformat()
    path = Path(f"Class_Summary_{today}.txt")
    path.write_text(summary)
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
