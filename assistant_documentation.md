# AI Desktop Voice Assistant - Technical Documentation
*Created: 2026-09-22 | Project: BCC-351 Mini Project*

## Table of Contents
- [Architecture Overview](#architecture-overview)
- [Core Components](#core-components)
- [Library Usage Analysis](#library-usage-analysis)
- [Command Processing Logic](#command-processing-logic)
- [Error Handling Strategy](#error-handling-strategy)
- [Future Enhancements](#future-enhancements)
- [Deployment Notes](#deployment-notes)

---

## Architecture Overview

The assistant implements a **command-query pattern** with four distinct phases:

```
1. Voice Capture → Speech-to-Text (Google API)
2. Command Parsing → Keyword matching + intent extraction  
3. Function Execution → System calls/API requests/Local operations
4. Voice Response → Text-to-Speech (SAPI5 via pyttsx3)
```

**Key Design Decisions:**
- **Online/Offline Hybrid**: Speech recognition requires internet, TTS works offline
- **Stateless design**: No database required; simple file storage for memory
- **Graceful degradation**: Fallbacks for missing components (local music → YouTube Music)
- **Platform targeting**: Windows-first with cross-platform path handling

---

## Core Components

### 1. TTS Engine (`pyttsx3`)
**Location**: Lines 32-48, 50-76

```python
# Engine Configuration
engine = pyttsx3.init()
engine.setProperty('rate', 150)   # 150 words/minute (vs default 200)
engine.setProperty('volume', 1.0) # Maximum volume
engine.setProperty('voice', voices[1].id)  # Zira (female) voice
```

**Why pyttsx3 over alternatives?**
- No API keys needed (offline SAPI5 engine)
- Cross-platform (Windows SAPI5, macOS NSSpeechSynthesizer, Linux eSpeak)
- Simple blocking interface (`runAndWait()`)

**Performance Considerations:**
- `init()` is expensive (~100-200ms) → cached in global variable
- `runAndWait()` blocks execution until speech completes
- Multiple `speak()` calls create natural pauses between sentences

### 2. Speech Recognition (`speech_recognition`)
**Location**: Lines 123-140

```python
r = sr.Recognizer()
r.pause_threshold = 1  # 1 second silence ends recording
audio = r.listen(source)  # Blocks until silence detected
query = r.recognize_google(audio, language="en-in")
```

**Configuration Options:**
- `pause_threshold=1`: Balanced between responsiveness and command length
- `language="en-in"`: Optimized for Indian English accents
- **Latency**: 2-5 seconds per recognition (API round-trip)

**Fallback Strategy:** Returns `"Try Again"` sentinel instead of crashing

### 3. Web Browser Control (`webbrowser`)
**Location**: Multiple sites handling (lines 198-214)

```python
wb.open("https://www.youtube.com")  # Direct URL
wb.get(chrome_path).open_new_tab(query)  # Chrome-specific tab
```

**URL Formats:** Always uses `https://` for reliability (bare domains fail on some Windows setups)

### 4. Screenshot System (`pyautogui`)
**Location**: Lines 110-121

```python
img = pyautogui.screenshot()
directory = Path.home() / "Pictures" / "Screenshots"  # Cross-platform
img.save(str(screenshot_path))  # Convert Path to string
```

**Path Strategy:** User's Pictures folder ensures write permissions

### 5. Wikipedia Integration (`wikipediaapi`)
**Location**: Lines 183-196

```python
wiki_wiki = wikipediaapi.Wikipedia('en')
result = wiki_wiki.page(query)
if result.exists():
    summary = result.summary[:200]  # First 200 characters
```

**Why not `wikipedia` library?**
- `wikipediaapi` has cleaner API
- Better page existence checking
- Structured summary extraction

### 6. Translation (`googletrans`)
**Location**: Lines 329-343

```python
translator = Translator()
translated = translator.translate(text, dest=target_language).text
```

**Limitation:** Unofficial API, subject to rate limits/blocking

---

## Command Processing Logic

### Pattern: Keyword-in-String Matching

```python
if "time" in query:
    time()
elif "date" in query:
    date()
# ...
```

**Advantages:**
- Simple implementation
- Fault-tolerant (partial matches work)
- No NLP dependencies

**Disadvantages:**
- No intent understanding
- Ambiguous queries not handled
- Exact word matching required

### Command Categories

| Category | Commands | Implementation |
|----------|----------|----------------|
| **System Info** | time, date | `datetime.now()` |
| **Web Search** | wikipedia, search | `wb.open()`, `wikipediaapi` |
| **Media Control** | play music | `os.startfile()`, `wb.open()` |
| **Browser** | open youtube, open chrome | `webbrowser`, path detection |
| **System Control** | screenshot, shutdown, lock | `pyautogui`, `os.system` |
| **Utilities** | remember, translate, joke | File I/O, `googletrans`, array selection |

### Specialized Handlers

#### Chrome Path Detection
```python
chrome_paths = [
    Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
    Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
    Path.home() / "AppData/Local/Google/Chrome/Application/chrome.exe"
]
```

**Why three paths?** Accounts for:
- 64-bit system default
- 32-bit Chrome on 64-bit Windows
- Per-user installation

#### Music Playback Strategy
```python
# 1. Check local Music folder
music_exists = song_dir.exists() and any(song_dir.iterdir())
# 2. Pick random file
# 3. Fallback to music.youtube.com
```

**Rationale:** Provides user value even without local music library

---

## Error Handling Strategy

### Multi-Layer Defense

```python
try:
    # Primary operation
    engine.say(audio)
    engine.runAndWait()
except RuntimeError:
    # Engine in bad state → reinitialize
    init_engine()
    if engine is not None:
        try:
            engine.say(audio)
            engine.runAndWait()
        except Exception:
            pass  # Silent failure
except Exception:
    pass  # Never crash on TTS failure
```

### Specific Error Cases

1. **TTS Engine Failure**: Reinitialize or silently skip
2. **Speech Recognition Failure**: Return "Try Again" sentinel
3. **File Not Found**: Inform user and continue
4. **API Failures**: Graceful message, no stack traces shown

### Sentinel Pattern
```python
if result != "Try Again":
    # Process valid command
```

---

## Security Considerations

### Current Status
- **No authentication** required (local desktop app)
- **No sensitive data** transmitted (except Google APIs)
- **File operations**: User's Pictures folder only
- **System commands**: Requires admin for shutdown commands

### Potential Improvements
1. **Environment variables** for API keys
2. **Input validation** for system commands
3. **Sandboxing** of os.system calls
4. **Logging** for security audits

---

## Performance Characteristics

### Time Measurements (Approximate)
| Operation | Time | Notes |
|-----------|------|-------|
| `init_engine()` | 150-250ms | One-time startup cost |
| `speak("short phrase")` | 500-1000ms | Varies by phrase length |
| `takecommand()` | 2000-5000ms | API latency dominates |
| `pyautogui.screenshot()` | 50-100ms | Fast, filesystem limited |
| `wikipediaapi.page()` | 500-1500ms | Wikipedia API response |

### Memory Usage
- **Base**: ~30MB Python interpreter
- **pyttsx3**: +10-15MB
- **speech_recognition**: +5MB
- **Total**: ~45-50MB idle

---

## Deployment Notes

### Dependencies (`requirements.txt`)
```
pyttsx3==2.90
SpeechRecognition==3.10.0
wikipediaapi==0.7.0
pyautogui==0.9.54
googletrans==4.0.0rc1
```

### Installation Issues

**Common Problem:** PyAudio on Python 3.13+
```python
# Workaround in code
try:
    import pyaudio
except ImportError:
    import pyaudio_compat
    sys.modules['pyaudio'] = pyaudio_compat
```

**Alternative:** Use `pipwin` for Windows PyAudio binaries

### Windows-Specific Commands
```python
# Shutdown/Restart
os.system("shutdown /r /t 1")   # Restart in 1 second
os.system("shutdown /h")        # Hibernate
os.system("shutdown /l")        # Log off

# Power States
os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Sleep
os.system("rundll32.exe user32.dll,LockWorkStation")          # Lock
```

---

## Future Enhancement Roadmap

### Priority 1 (Easy Implementation)
1. **Weather API** - OpenWeatherMap integration
2. **Calculator** - Basic arithmetic via voice
3. **System Monitor** - CPU/RAM display via `psutil`
4. **Timer/Stopwatch** - Threading-based time tracking

### Priority 2 (Medium Complexity)
5. **Email Sender** - SMTP via `smtplib`
6. **File Search** - `os.walk()` file finding
7. **News Headlines** - NewsAPI integration
8. **Currency Converter** - Forex API

### Priority 3 (Advanced)
9. **ChatGPT Integration** - OpenAI API for conversational responses
10. **Spotify Control** - `spotipy` library integration
11. **Window Management** - `pygetwindow` for app control
12. **Custom Wake Word** - Hotword detection

### Implementation Pattern Example

```python
def weather():
    import requests
    api_key = os.getenv("WEATHER_API_KEY")
    city = "New Delhi"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    temp = data["main"]["temp"] - 273.15  # Kelvin to Celsius
    speak(f"Temperature in {city} is {temp:.1f} degrees Celsius")
```

---

## Testing Strategy

### Manual Test Commands
```python
# Test all features
test_commands = [
    "what time is it",
    "what's the date",
    "wikipedia artificial intelligence",
    "open youtube",
    "play music",
    "screenshot",
    "remember that meeting at 3pm",
    "translate hello to french",
    "tell me a joke",
    "search python tutorials"
]
```

### Automated Testing Considerations
1. **Mock microphone input** for CI/CD
2. **Disable TTS** in test mode
3. **Mock external APIs** (Google Speech, Wikipedia)
4. **Test path resilience** across OSes

---

## Code Quality Metrics

### Current Strengths
✅ **Separation of concerns** - Clean function boundaries  
✅ **Error resilience** - Graceful degradation patterns  
✅ **Cross-platform paths** - Pathlib usage  
✅ **Simple maintenance** - No complex dependencies  

### Areas for Improvement
⚠ **Code duplication** - Similar web opening patterns  
⚠ **Hardcoded paths** - Chrome detection could be configurable  
⚠ **Magic strings** - Command phrases scattered  
⚠ **No logging** - Debugging requires print statements  

### Refactoring Opportunities
```python
# Extract to command registry pattern
COMMAND_REGISTRY = {
    "time": time_function,
    "date": date_function,
    "wikipedia": wikipedia_search,
    # ...
}

# Process query
for keyword, handler in COMMAND_REGISTRY.items():
    if keyword in query:
        handler(query)
        break
```

---

## Appendix: Complete Command Reference

| Command Pattern | Example | Function Called |
|-----------------|---------|-----------------|
| `"time"` | "what time is it" | `time()` |
| `"date"` | "what's the date today" | `date()` |
| `"wikipedia"` | "wikipedia machine learning" | Wikipedia search |
| `"search"` | "search python tutorials" | Google search |
| `"open youtube"` | "open youtube" | `wb.open("youtube.com")` |
| `"play music"` | "play music" | Local music or YouTube Music |
| `"screenshot"` | "take screenshot" | `screenshot()` |
| `"remember that"` | "remember that meeting at 3" | Save to data.txt |
| `"translate"` | "translate hello to spanish" | Google Translate |
| `"tell me a joke"` | "tell me a joke" | `tell_joke()` |
| `"open chrome"` | "open chrome" | Chrome launcher |
| `"search on chrome"` | "search on chrome python" | Chrome-specific search |

---

*Documentation generated: 2026-09-22*  
*Project: AI Desktop Voice Assistant - BCC-351 Mini Project*  
*Maintainer: [Your Name Here]*  
*Version: 1.0.0*
