# 🎯 AI-Based Habit Tracking Agent

An agentic AI system that logs, analyzes, and gives personalized motivational feedback on daily habits — built using a multi-agent architecture (CrewAI), powered by Google Gemini, and deployed as a public web app.

**🔗 Live App:** [Add your Render URL here]

---

## 📚 Academic Details

| Field | Detail |
|---|---|
| **Name** | Harman Saini |
| **PRN** | 24070521056 |
| **Course** | Agentic AI (Flexi Credit) |
| **Semester** | 5th Semester |
| **Project Type** | Mini Project |

---

## 📖 Overview

This project implements a **multi-agent AI system** that helps users track daily habits through natural conversation. Instead of manually filling forms, the user simply tells the assistant what they did (e.g., *"I did yoga today"*), and a team of specialized AI agents work together to log the entry, analyze the pattern, and respond with personalized coaching feedback — all through a clean chat interface with a live analytics dashboard.

The system is built entirely around **agentic AI principles** taught in the course: role-based agent design, tool-augmented reasoning, sequential task orchestration, and LLM-powered decision making — deployed as a real, publicly accessible web application.

---

## 🧠 Multi-Agent Architecture

The system uses **CrewAI** to orchestrate three specialized agents, each with a single clear responsibility:

```
User Input (Gradio Chat)
        │
        ▼
┌─────────────────────┐
│   1. LOGGER AGENT     │  → Extracts habit name + status (done/missed)
│                      │     → Tool: writes entry to SQLite database
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│   2. ANALYST AGENT    │  → Reads habit history from database
│                      │     → Tool: calculates streak & completion %
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│   3. COACH AGENT      │  → Takes stats as context
│                      │     → Generates short, personalized motivational feedback
└─────────────────────┘
        │
        ▼
Gradio Output: Chat reply + live Dashboard (streaks, completion %)
```

**Why this design?** Each agent has one clear job (logging, analysis, or coaching), making the system modular, easy to debug, and easy to explain — while still demonstrating core agentic AI concepts: task delegation, tool use, sequential process orchestration, and context-passing between agents.

---

## ⚙️ Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| Agent Framework | **CrewAI** | Multi-agent orchestration |
| LLM | **Google Gemini 3.6 Flash** | Natural language understanding & generation |
| Database | **SQLite** | Lightweight storage for habit logs |
| UI | **Gradio** | Chat interface + analytics dashboard |
| Deployment | **Render (Web Service)** | Free public hosting |
| Language | **Python 3.12** | Core implementation |

---

## ✨ Features

- 💬 **Conversational habit logging** — no forms, just natural language
- 🤖 **Multi-agent pipeline** — logging, analysis, and coaching handled by separate specialized agents
- 📊 **Live dashboard** — streaks and completion percentage per habit, refreshable on demand
- 🛠️ **Custom tools** — agents use purpose-built tools to read/write structured data
- 🛡️ **Graceful error handling** — API quota (429) and service (503) errors are caught; habit logging still succeeds even if AI feedback is temporarily unavailable
- 🌐 **Publicly deployed** — accessible via a shareable web link, no installation needed

---

## 📁 Project Structure

```
habit_agent/
├── app.py             # Gradio UI (chat + dashboard)
├── crew_setup.py       # Agent, task, and crew definitions
├── tools.py            # Custom CrewAI tools (logging, analysis)
├── db.py               # SQLite database layer
├── requirements.txt    # Python dependencies
├── .python-version     # Pinned Python version (3.12) for deployment
├── .gitignore          # Excludes .env, venv, habits.db, cache files
└── README.md
```

---

## 🚀 Running Locally

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd habit_agent

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini API key
# Create a .env file in the project root:
echo GEMINI_API_KEY=your_key_here > .env

# 5. Run the app
python app.py
```

The app will launch locally at `http://127.0.0.1:7860`.

---

## 🌍 Deployment

Deployed on **Render** as a free Web Service:
- Build Command: `pip install -r requirements.txt`
- Start Command: `python app.py`
- Environment Variable: `GEMINI_API_KEY`
- App binds to `0.0.0.0` and Render's dynamic `PORT` for compatibility

> **Note:** On Render's free tier, the app sleeps after periods of inactivity and takes ~30–50 seconds to wake up on the next request. The SQLite database also resets on redeploys/restarts, since free-tier storage is not persistent — logged data is meant for live demonstration rather than long-term storage in this version.

---

## 🔭 Future Scope

- Replace SQLite with a persistent cloud database (e.g., Supabase/Postgres) for permanent data storage across restarts
- Add multi-user support with authentication
- Add a reminder/notification agent for daily check-ins
- Expand analysis with weekly/monthly trend visualizations

---

## 👤 Author

**Harman Saini**
PRN: 24070521056
B.Tech CSE (AI/ML), 5th Semester
Agentic AI Course — Flexi Credit
