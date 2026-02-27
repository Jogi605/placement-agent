# 🚀 Placement Agent

This repository contains draft implementations and experimental
iterations of building an AI Agent for placement preparation.

It demonstrates how to build and run AI agents locally using:

-   Python
-   LangChain
-   Ollama (local LLM execution)
-   Tavily (web search integration)
-   ReportLab (PDF generation)

> ⚠️ This project is for learning and experimentation purposes only. It
> is not production-ready.

------------------------------------------------------------------------

## 📌 Features

-   Local LLM-powered AI agent
-   Tool-based agent architecture using LangChain
-   Web search integration using Tavily
-   PDF report generation using ReportLab
-   Multiple experimental iterations of agent design

------------------------------------------------------------------------

## 🛠 System Requirements

### Basic Tools

1.  Git\
2.  VS Code\
3.  GitHub Account\
4.  Python 3.10+\
5.  Ollama

### Python Libraries

-   langchain\
-   tavily-python\
-   reportlab

------------------------------------------------------------------------

# 🖥 Installation & Setup (Step-by-Step)

## 1️⃣ Install Git

Download from:\
https://git-scm.com/downloads

Verify installation:

git --version

------------------------------------------------------------------------

## 2️⃣ Install Python (3.10+)

Download from:\
https://www.python.org/downloads/

Verify:

python --version

------------------------------------------------------------------------

## 3️⃣ Install VS Code

Download from:\
https://code.visualstudio.com/

Recommended Extensions: - Python Extension - GitLens (optional)

------------------------------------------------------------------------

## 4️⃣ Install Ollama

Download from:\
https://ollama.ai

Verify installation:

ollama --version

------------------------------------------------------------------------

## 5️⃣ Pull Required Model (Llama3)

ollama pull llama3

Test it:

ollama run llama3

If it responds, Ollama is working correctly.

------------------------------------------------------------------------

## 6️⃣ Clone the Repository

git clone `<your-repo-url>`{=html}\
cd placement-agent

------------------------------------------------------------------------

## 7️⃣ Create Virtual Environment

### Windows

python -m venv venv\
venv`\Scripts`{=tex}`\activate`{=tex}

### Mac/Linux

python3 -m venv venv\
source venv/bin/activate

------------------------------------------------------------------------

## 8️⃣ Install Dependencies

If requirements.txt exists:

pip install -r requirements.txt

Otherwise install manually:

pip install langchain tavily-python reportlab

------------------------------------------------------------------------

## 9️⃣ Setup Tavily API

1.  Create an account at:\
    https://tavily.com

2.  Generate your API key.

3.  Set environment variable:

### Windows (PowerShell)

setx TAVILY_API_KEY "your_api_key_here"

Restart terminal after setting.

### Mac/Linux

export TAVILY_API_KEY="your_api_key_here"

------------------------------------------------------------------------

# ▶️ Running the Agent

Make sure:

-   Virtual environment is activated\
-   Ollama is running\
-   llama3 model is pulled\
-   Tavily API key is set

Run:

python main.py

------------------------------------------------------------------------

## 📂 Example Project Structure

placement-agent/ │ ├── main.py\
├── agent/\
│ ├── tools.py\
│ ├── prompts.py\
│ └── chains.py\
│ ├── reports/\
├── requirements.txt\
└── README.md

------------------------------------------------------------------------

## 🧠 How It Works (High Level)

1.  User provides input (e.g., company name or topic).\
2.  Agent processes input using:
    -   Local LLM via Ollama
    -   Web search via Tavily
3.  LangChain orchestrates tools and reasoning.\
4.  Output may be structured and optionally exported as a PDF.

------------------------------------------------------------------------

## 🎯 Purpose of This Repository

-   Learning reference for building AI agents\
-   Playground for experimenting with LangChain\
-   Starting point for placement-preparation assistants\
-   Template for building custom tool-augmented agents

------------------------------------------------------------------------

## 🔮 Possible Extensions

-   Add memory support\
-   Integrate vector database (ChromaDB)\
-   Implement RAG pipeline\
-   Multi-agent workflows\
-   Structured output parsing\
-   Logging and evaluation\
-   Web UI (Streamlit / FastAPI)

------------------------------------------------------------------------

⭐ Happy Building!
