"""
Future Features for AI Desktop Voice Assistant
This file documents suggested features that can be added to assistant.py
"""

SUGGESTED_FEATURES = [
    {
        "feature": "Weather Lookup",
        "command": "what's the weather",
        "description": "Fetch current weather using OpenWeatherMap API",
        "library": "requests",
        "difficulty": "Easy"
    },
    {
        "feature": "News Headlines",
        "command": "give me news",
        "description": "Fetch latest news headlines from a news API",
        "library": "newsapi",
        "difficulty": "Easy"
    },
    {
        "feature": "Calculator",
        "command": "calculate 5 times 10",
        "description": "Perform basic arithmetic calculations via voice",
        "library": "built-in",
        "difficulty": "Easy"
    },
    {
        "feature": "Email Sender",
        "command": "send email to john",
        "description": "Compose and send emails via voice",
        "library": "smtplib",
        "difficulty": "Medium"
    },
    {
        "feature": "System Monitor",
        "command": "show system info",
        "description": "Display CPU usage, RAM, disk space, battery status",
        "library": "psutil",
        "difficulty": "Easy"
    },
    {
        "feature": "Shutdown/Restart",
        "command": "shutdown computer",
        "description": "Shutdown or restart the PC via voice",
        "library": "os / subprocess",
        "difficulty": "Easy"
    },
    {
        "feature": "Timer/Stopwatch",
        "command": "set timer for 5 minutes",
        "description": "Voice-controlled timer and stopwatch",
        "library": "threading / time",
        "difficulty": "Easy"
    },
    {
        "feature": "Note Taking",
        "command": "take note",
        "description": "Voice-dictated notes saved to file",
        "library": "built-in",
        "difficulty": "Easy"
    },
    {
        "feature": "YouTube Search & Play",
        "command": "play video on youtube",
        "description": "Search and open specific YouTube videos",
        "library": "webbrowser + YouTube API",
        "difficulty": "Medium"
    },
    {
        "feature": "Currency Converter",
        "command": "convert 100 dollars to rupees",
        "description": "Real-time currency conversion",
        "library": "forex-python",
        "difficulty": "Medium"
    },
    {
        "feature": "Map Directions",
        "command": "directions to airport",
        "description": "Open Google Maps with directions",
        "library": "webbrowser",
        "difficulty": "Easy"
    },
    {
        "feature": "ChatGPT Integration",
        "command": "ask chatgpt what is AI",
        "description": "Conversational AI responses using OpenAI API",
        "library": "openai",
        "difficulty": "Hard"
    },
    {
        "feature": "File Search",
        "command": "find report.docx",
        "description": "Search for files across the system",
        "library": "os / pathlib",
        "difficulty": "Medium"
    },
    {
        "feature": "Alarm/Reminder",
        "command": "set alarm for 7 AM",
        "description": "Set voice-activated alarms and reminders",
        "library": "datetime / threading",
        "difficulty": "Medium"
    },
    {
        "feature": "Window Management",
        "command": "close chrome",
        "description": "Minimize, maximize, or close specific windows",
        "library": "pygetwindow",
        "difficulty": "Medium"
    },
    {
        "feature": "Stock Price Checker",
        "command": "check apple stock price",
        "description": "Fetch live stock market prices",
        "library": "yfinance",
        "difficulty": "Easy"
    },
    {
        "feature": "Password Generator",
        "command": "generate password",
        "description": "Create strong random passwords",
        "library": "secrets / random",
        "difficulty": "Easy"
    },
    {
        "feature": "Spotify Control",
        "command": "pause music",
        "description": "Control Spotify playback (play, pause, next)",
        "library": "spotipy",
        "difficulty": "Hard"
    },
    {
        "feature": "Clipboard Copy/Paste",
        "command": "copy this text",
        "description": "Copy text to clipboard via voice",
        "library": "pyperclip",
        "difficulty": "Easy"
    },
    {
        "feature": "Daily Routine Reminder",
        "command": "set routine reminder",
        "description": "Schedule daily task reminders with custom times",
        "library": "schedule",
        "difficulty": "Medium"
    },
]

# Print summary
if __name__ == "__main__":
    print("=" * 60)
    print("SUGGESTED FUTURE FEATURES FOR VOICE ASSISTANT")
    print("=" * 60)
    for i, f in enumerate(SUGGESTED_FEATURES, 1):
        print(f"\n{i}. {f['feature']}")
        print(f"   Command: \"{f['command']}\"")
        print(f"   Library: {f['library']}")
        print(f"   Difficulty: {f['difficulty']}")
    print(f"\nTotal: {len(SUGGESTED_FEATURES)} suggested features")
