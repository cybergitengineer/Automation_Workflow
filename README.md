
# 🧠 Automation Suite (AI-Driven Daily Agents)

This project contains six AI-powered agents designed to automate your weekday tasks related to job search, learning, research, and productivity. It includes a Docker-based setup and optional integration with n8n.

---

## 📁 Folder Structure

```
/automation-suite/
│
├── Dockerfile
├── docker-compose.yml
│
├── Job_Hunter_Agent.py
├── Study_Assistant_Agent.py
├── Business_Research_Agent.py
├── News_Agent.py
├── Class_Summarizer_Agent.py
├── Project_Builder_Agent.py
│
├── class_transcript.txt       # Input file for Class Summarizer Agent
└── README.md
```

---

## 🚀 Agents Overview

| Agent | Purpose |
|-------|---------|
| `Job_Hunter_Agent.py` | Scrapes jobs, tailors resumes, emails results |
| `Study_Assistant_Agent.py` | Generates CISSP flashcards and summaries |
| `Business_Research_Agent.py` | Performs market research + projections |
| `News_Agent.py` | Summarizes top tech/cyber news headlines |
| `Class_Summarizer_Agent.py` | Summarizes lecture transcripts |
| `Project_Builder_Agent.py` | Builds GitHub-ready project scaffolds |

---

## 🐳 Running with Docker

### 1. Build the container
```bash
docker-compose build
```

### 2. Run all agents
```bash
docker-compose up
```

Each agent runs in its own container. Logs are streamed to your terminal.

---

## 🔑 Environment Variables

Set the following in a `.env` file or pass them at runtime:

```
OPENAI_API_KEY=your_openai_key_here
EMAIL_PASSWORD=your_email_password_here
```

---

## ✍️ Prerequisites

- Docker & Docker Compose installed
- Optional: Python 3.10+ and pip if running agents manually

---

## 🧩 Optional: n8n Integration

You can integrate this with [n8n](https://n8n.io) using:
- HTTP request nodes (if you add Flask wrappers)
- Shell command nodes (to run containers)
- File triggers (e.g., Google Drive upload → trigger summarizer)

---

## 📦 Coming Soon (Ideas)

- Scheduler for agents using cron or APScheduler
- Flask API wrappers for real-time agent calls
- Web UI to manage agent configs and inputs

---

## 📬 Contact

Built for AI + Cybersecurity automation. Adapt, fork, and build on it!
