# Jarvis Virtual Assistant

A Python-based voice assistant that can perform everyday tasks using speech recognition, automation, and API integrations.

## Features

- Voice command recognition
- Text-to-speech responses
- Open websites using voice commands
- Play music through voice commands
- Google and YouTube search
- Fetch current time and date
- Open system applications (Notepad, Calculator, Paint)
- Wikipedia information lookup
- Latest news fetching
- AI-powered responses using Gemini

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- Wikipedia API
- News API
- Google Gemini API
- Requests

## Project Structure

```
Jarvis/
│
├── main.py              # Main assistant logic
├── Ai.py                # AI response handling
├── musicLibrary.py      # Music links database
├── test.py              # Testing files
├── test2.py             # Testing files
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/jaivardhansingh0502/jarvis-virtual-assistant.git
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file:

```
NEWS_API_KEY=your_news_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### 5. Run Jarvis

```bash
python main.py
```

## Future Improvements

- Add wake word detection
- Improve natural language understanding
- Add more automation features
- Create a graphical user interface
- Add user customization options

## Author

Jaivardhan Singh
