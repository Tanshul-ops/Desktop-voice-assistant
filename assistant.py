import sys

# PyAudio compatibility fallback - MUST be before speech_recognition import
try:
    import pyaudio
except ImportError:
    import pyaudio_compat
    sys.modules['pyaudio'] = pyaudio_compat

import pyttsx3
import datetime
import html.parser
# Monkey-patch for Python 3.13+ compatibility with older dependencies
if not hasattr(sys.modules.get('html.parser', html.parser), 'HTMLParseError'):
    sys.modules.setdefault('html.parser', html.parser).HTMLParseError = Exception
if 'cgi' not in sys.modules:
    import html
    class DummyCGI:
        def escape(self, s, quote=True):
            return html.escape(s, quote=quote)
    sys.modules['cgi'] = DummyCGI()

import speech_recognition as sr
import wikipediaapi
import webbrowser as wb
import os
import random
import pyautogui
from pathlib import Path
from googletrans import Translator

# Import language converter for multilingual support
try:
    from language_converter import reply_in_same_language, detect_language
    LANGUAGE_CONVERTER_AVAILABLE = True
except ImportError:
    LANGUAGE_CONVERTER_AVAILABLE = False
    print("[Assistant] Language converter not available, using English only")

engine = None

def init_engine():
    """Initialize the TTS engine with proper settings."""
    global engine
    try:
        engine = pyttsx3.init()
        # Set properties for better audio
        engine.setProperty('rate', 150)  # Speaking rate
        engine.setProperty('volume', 1.0)  # Max volume

        # Try to use a specific voice (Zira is usually clearer)
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)  # Microsoft Zira
    except Exception:
        engine = None

def speak(audio, user_text=None):
    """
    Speak the given text using TTS engine.
    If user_text is provided and language_converter is available,
    detect user's language and translate response to match.
    """
    global engine

    # Use language converter to match user's language
    if user_text and LANGUAGE_CONVERTER_AVAILABLE:
        audio = reply_in_same_language(user_text, audio)

    # Print what will be spoken (force UTF-8 safe output)
    try:
        safe_audio = audio.encode("ascii", "replace").decode("ascii") if isinstance(audio, str) else str(audio)
        print("[SPEAKING] " + safe_audio)
    except Exception:
        print("[SPEAKING] (non-ASCII content - Hindi/other language)")

    # Re-initialize engine if it's None or seems unresponsive
    if engine is None:
        init_engine()
        if engine is None:
            return

    try:
        engine.say(audio)
        engine.runAndWait()
    except RuntimeError:
        # Engine may be in a bad state, reinitialize
        init_engine()
        if engine is not None:
            try:
                engine.say(audio)
                engine.runAndWait()
            except Exception:
                pass
    except Exception:
        pass

# Initialize engine at startup
init_engine()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!!")

    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tomorrow")

    speak("Quan at your service, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    # Use dynamic path based on user's Pictures directory
    directory = Path.home() / "Pictures" / "Screenshots"

    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)

    # Fix: Use proper path joining with Path
    screenshot_path = directory / "screenshot.png"
    img.save(str(screenshot_path))
    print(f"Screenshot saved to: {screenshot_path}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why did the computer go to therapy? It had too many bytes of emotional baggage!",
        # Add more jokes to the list as needed
    ]

    joke = random.choice(jokes)
    speak(joke)

if __name__== "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm Quan, your desktop voice assistant.", query)

        elif "how are you" in query:
            speak("I'm fine sir, What about you?", query)

        elif "fine" in query or "good" in query:
            speak("Glad to hear that sir!!", query)

        elif "search" in query:
            # Direct search command: "search python tutorials"
            search_term = query.replace("search for", "").replace("search", "").strip()
            if search_term:
                wb.open(f"https://www.google.com/search?q={search_term}")
            else:
                speak("What should I search?", query)
                result = takecommand()
                if result != "Try Again":
                    wb.open(f"https://www.google.com/search?q={result}")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...", query)
                query = query.replace("wikipedia","")
                wiki_wiki = wikipediaapi.Wikipedia('en')
                result = wiki_wiki.page(query)
                if result.exists():
                    summary = result.summary[:200]  # Considering first 200 characters of the summary
                    speak(summary, query)
                else:
                    speak("Can't find this page sir, please ask something else", query)
            except Exception as e:
                print("Error:", e)
                speak("Can't find this page sir, please ask something else", query)

        elif "open youtube" in query:
            wb.open("https://www.youtube.com")
        elif "open instagram" in query:
            wb.open("https://www.instagram.com")
        elif "open facebook" in query:
            wb.open("https://www.facebook.com")
        elif "open whatsapp" in query:
            wb.open("https://web.whatsapp.com")
        elif "open gmail" in query:
            wb.open("https://mail.google.com")
        elif "open github" in query:
            wb.open("https://github.com")
        elif "open google" in query:
            wb.open("google.com")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            # Check for music platforms first
            song_dir = Path.home() / "Music"
            music_exists = song_dir.exists() and any(song_dir.iterdir())

            if music_exists:
                songs = [f for f in os.listdir(song_dir) if os.path.isfile(song_dir / f)]
                if songs:
                    selected_song = random.choice(songs)
                    song_path = song_dir / selected_song
                    os.startfile(str(song_path))
                    speak("Playing music from your library", query)

            # No local music - open web music platform
            speak("No local music found. Opening YouTube Music", query)
            wb.open("https://music.youtube.com")

        elif "open chrome" in query:
            # Check multiple possible Chrome installation paths
            chrome_paths = [
                Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
                Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
                Path.home() / "AppData/Local/Google/Chrome/Application/chrome.exe"
            ]

            chrome_found = False
            for chrome_path in chrome_paths:
                if chrome_path.exists():
                    os.startfile(str(chrome_path))
                    chrome_found = True
                    break

            if not chrome_found:
                speak("Chrome not found, opening default browser instead", query)
                wb.open("https://www.google.com")

        elif "search on chrome" in query:
            try:
                speak("What should I search?")

                # Check multiple possible Chrome installation paths
                chrome_paths = [
                    Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
                    Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
                    Path.home() / "AppData/Local/Google/Chrome/Application/chrome.exe"
                ]

                chrome_path = None
                for path in chrome_paths:
                    if path.exists():
                        chrome_path = str(path)
                        break

                search = takecommand()

                if chrome_path:
                    wb.get(f'"{chrome_path}" %s').open_new_tab(search)
                else:
                    # Fallback to default browser
                    wb.open(f"https://www.google.com/search?q={search}")

            except Exception as e:
                speak("Can't open now, please try again later.")


        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that " + data)
            # Fix: Use context manager and append mode
            with open("data.txt", "a") as remember:
                remember.write(data + "\n")

        elif "do you remember anything" in query:
            # Fix: Use context manager and properly read content
            try:
                with open("data.txt", "r") as remember:
                    content = remember.read()
                    if content.strip():
                        speak("You told me to remember that " + content)
                    else:
                        speak("You haven't asked me to remember anything yet")
            except FileNotFoundError:
                speak("You haven't asked me to remember anything yet")

        elif "screenshot" in query:
            screenshot()
            speak("I've taken a screenshot, please check it")

        elif "offline" in query:
            quit()
        elif "exit" in query:
            quit()
        elif "goodbye" in query:
            quit()
        elif "quit" in query:
            quit()
        elif "shutdown" in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 1")  # Shutdown the system
            quit()
        elif "restart" in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 1")  # Restart the system immediately
            quit()
        elif "hibernate" in query:
            speak("Hibernating the system")
            os.system("shutdown /h")  # Hibernate the system
            quit()
        elif "sleep" in query:
            speak("Putting the system to sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Sleep the system
            quit()
        elif "lock" in query:
            speak("Locking the workstation")
            os.system("rundll32.exe user32.dll,LockWorkStation")  # Lock the system
        elif "log off" in query or "sign out" in query:
            speak("Logging off")
            os.system("shutdown /l")  # Log off the system
            quit()

        elif "tell me a joke" in query or "joke" in query:
            tell_joke()

        # Translation functionality
        elif "translate" in query:
            speak("What would you like me to translate?")
            text_to_translate = takecommand()

            speak("To which language would you like to translate?")
            target_language = takecommand()

            translator = Translator()

            try:
                translated_text = translator.translate(text_to_translate, dest=target_language).text
                speak(f"The translation is: {translated_text}")
            except Exception as e:
                speak("Sorry, I couldn't perform the translation. Please try again.")