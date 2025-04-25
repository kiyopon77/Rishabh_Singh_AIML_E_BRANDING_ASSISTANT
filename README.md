# 🎨 AI Branding Assistant

An AI-powered web application that helps small businesses develop their brand image by recommending aesthetic elements like colors, fonts, and design themes — all based on natural language input.

---

## 🚀 Project Overview

This project uses a **LLaMA-based model** integrated with **Flask** to generate branding recommendations from user descriptions. The UI mimics a ChatGPT-style conversation interface for a familiar and user-friendly experience.

---

## 🛠️ Features

- 🧠 Natural language input box for business descriptions
- 🎨 AI-generated color palettes, font ideas, and aesthetic suggestions
- 💬 Chat-style user interface inspired by ChatGPT
- 📦 Easy deployment with Flask

---

## 🖼️ Demo

> Coming soon: Video demo link & screenshots

---

## 📂 Directory Structure

├── static/ # CSS and assets (optional)
├── templates/
│ └── branding_form.html # Main HTML template with chat UI
├── app.py # Flask app logic
├── requirements.txt # Python dependencies
└── README.md

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/branding-assistant.git
cd branding-assistant
```


## Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## 2. Install Requirements
```bash
pip install -r requirements.txt
```

## 4. Run the Flask app
```bash
python app.py
```
---

## 🤖 LLaMA Model Integration
The backend connects to a running LLaMA server to generate branding suggestions. Ensure that your LLaMA Flask server is up and accessible at the endpoint configured in app.py (http://localhost:8080/completion by default).


## 📌 Future Improvements
- Logo generation via GANs

- Multi-language support

- User history and login system

- SaaS platform deployment

## 👨‍💻 Authors
- Rishabh Rajkishor Singh

- Harshit Rawat

- Omm Routray

Project under guidance of Mr. Amar Saraswat\
🌟 2nd Year AIML Department – College AI Project
