[readme_1.md](https://github.com/user-attachments/files/35191019/readme_1.md)# Quan — Desktop Voice Assistant

A Python-based desktop voice assistant ([Tanshul-ops/Desktop-voice-assistant](https://github.com/Tanshul-ops/Desktop-voice-assistant)) that listens to spoken commands through the microphone, executes desktop and web actions, and speaks responses aloud.

## Features

- **Voice Input & Speech Output**: Captures microphone audio via `SpeechRecognition` and synthesizes spoken replies via `pyttsx3`.
- **Time & Date**: Speaks the current local time and calendar date using `datetime`.
- **Wikipedia Summaries**: Looks up topics with `wikipediaapi` and reads concise article summaries.
- **Web Browsing**: Opens sites such as YouTube, Google, Stack Overflow, and GitHub via `webbrowser`.
- **Local Music Playback**: Picks and plays audio files from your `Music` directory (`os`, `random`, `pathlib`).
- **Screenshot Capture**: Captures and saves desktop screenshots with `pyautogui`.
- **Persistent Notes (`data.txt`)**: Appends and recalls user notes saved in `data.txt`.
- **Text Translation**: Translates phrases into Hindi using `googletrans`.

## Requirements

- **Python**: Python 3.6+
- **Audio Hardware**: Microphone and speakers/headphones with desktop microphone permission enabled.
- **Dependencies**:
  - `pyttsx3`
  - `SpeechRecognition`
  - `PyAudio` (with `pyaudio_compat.py` / `sounddevice` & `numpy` fallback support)
  - `wikipedia-api` (`wikipediaapi`)
  - `googletrans`
  - `pyautogui`

## Setup & Run

```bash
git clone https://github.com/Tanshul-ops/Desktop-voice-assistant.git
cd Desktop-voice-assistant
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python assistant.py
```

If `PyAudio` fails to install, install `sounddevice` and `numpy` for `pyaudio_compat.py`:

```bash
pip install sounddevice numpy
```
