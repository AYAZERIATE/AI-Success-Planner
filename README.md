#  AI Success Planner

A command-line career assistant powered by a **local AI model (Ollama)**. It helps you generate a CV, prepare for interviews, discover job opportunities, write professional letters, find the best cities to work in, and build a personalized career roadmap — all offline, without relying on external APIs.

---

##  Features

| # | Module | Description |
|---|--------|-------------|
| 1 | **AI CV Generator** | Collects your personal/professional info and generates a modern, well-structured CV in Markdown format. |
| 2 | **AI Interview Helper** | Generates common software developer interview questions along with sample answers. |
| 3 | **AI Job Maker** | Suggests the best job opportunities in your field and country, with required skills and growth potential. |
| 4 | **AI Professional Letter Generator** | Writes formal letters (motivation, resignation, recommendation, etc.) tailored to your details. |
| 5 | **AI Job Location Helper** | Recommends the best cities in your country for your target job, with hiring industries and reasoning. |
| 6 | **AI Career Roadmap Generator** | Builds a month-by-month learning roadmap (3, 6, or 12 months) to reach your dream career. |

---

##  Tech Stack

- **Python 3.10+**
- **[Ollama](https://ollama.com)** — for running a local LLM
- Model used: `llama3.2` (configurable)

---

##  Project Structure

```
ai-success-planner/
├── main.py
├── ai/
│   ├── __init__.py
│   ├── ollama_client.py       # Core function that talks to the Ollama model
│   ├── cv_generator.py        # CV generator module
│   ├── interview_helper.py    # Interview Q&A generator
│   ├── job_makers.py          # Job opportunity finder
│   ├── letter_generator.py    # Professional letter writer
│   ├── map_helper.py          # Job location/city recommender
│   └── roadmap_generator.py   # Career roadmap generator
└── README.md
```

---

## ⚙️ Prerequisites

1. **Install Python 3.10+**
2. **Install Ollama** → [https://ollama.com/download](https://ollama.com/download)
3. **Pull the model used by the app:**
   ```bash
   ollama pull llama3.2
   ```
4. **Install the Python Ollama client:**
   ```bash
   pip install ollama
   ```

---

##  Usage

1. Make sure Ollama is running in the background.
2. Launch the app:
   ```bash
   python main.py
   ```
3. Choose an option from the menu:
   ```
   ==================================================
           AI SUCCESS PLANNER
   ==================================================
   1. AI CV generator
   2. AI Interview Helper
   3. AI Job Maker
   4. AI Professional Letter Generator
   5. AI Job Location Helper
   6. AI Career Roadmap Generator
   0. Exit
   ```
4. Follow the prompts — the AI response will be printed directly in your terminal.

---

##  Example

**Career Roadmap Generator**
```
Enter your dream career: Full Stack Developer
Enter roadmap duration (3, 6, or 12 months): 6

========== YOUR CAREER ROADMAP ==========
Month 1: HTML, CSS, JavaScript fundamentals...
Month 2: React.js basics + first project...
...
```

---

## 🧩 Configuration

The model name is set in `ai/ollama_client.py`:

```python
MODEL_NAME = "llama3.2"
```

Change this to any model you have pulled locally (e.g. `mistral`, `phi3`, `llama3`).

---

##  Roadmap / Ideas for Improvement

- [ ] Export generated CVs directly to PDF/Word instead of printing Markdown
- [ ] Save generated letters/roadmaps to files automatically
- [ ] Add a simple GUI (Tkinter or a small Flask web app)
- [ ] Add error handling for empty user input

---

##  Author

Developed by **Aya** — Full Stack Web Development student .

---

##  License

This project is open for personal and educational use.
