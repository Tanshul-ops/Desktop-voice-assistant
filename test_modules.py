"""
Clean test script for all 6 modules + language_converter + assistant integration.
Run: python test_modules.py
Output is written to test_results.txt so non-ASCII (Hindi) is preserved.
"""
import sys, io

# Redirect stdout to UTF-8 file so Hindi text is captured correctly
out = io.TextIOWrapper(open("test_results.txt", "w", encoding="utf-8"), newline="")
sys.stdout = out

def P(*args):
    """Safe print that never raises on non-ASCII."""
    try:
        print(*args)
    except UnicodeEncodeError:
        print(" ".join(str(a).encode("ascii", "replace").decode("ascii") for a in args))

P("=" * 60)
P("MODULE 1: langdetect")
P("=" * 60)
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

tests = [
    "Hello how are you",
    "namaste",
    "what time is it",
    "bonjour",
    "hola",
    "Guten Tag",
    "mera assignment ho gaya",
    "kya hai aapka naam",
]
for t in tests:
    try:
        print(f"  {t!r:30} -> {detect(t)}")
    except Exception as e:
        print(f"  {t!r:30} -> ERROR: {type(e).__name__}: {e}")

P()
P("=" * 60)
P("MODULE 2: pyttsx3 (TTS engine)")
P("=" * 60)
import pyttsx3
e = pyttsx3.init()
P("  Engine created OK")
P("  Rate:", e.getProperty("rate"))
P("  Volume:", e.getProperty("volume"))
P("  Voices available:", len(e.getProperty("voices")))
for v in e.getProperty("voices"):
    P(f"    - {v.name}")
P()
P("=" * 60)
P("MODULE 3: googletrans (translation)")
P("=" * 60)
from googletrans import Translator
tr = Translator()
pairs = [("Hello", "hi"), ("I am fine", "hi"), ("What is the time", "hi"),
         ("Namaste", "en"), ("mera assignment ho gaya", "en")]
for src, dst in pairs:
    out_text = tr.translate(src, dest=dst).text
    out_enc = out_text.encode("ascii", "replace").decode("ascii")
    P(f"  {src!r:25} -> [{dst}] {out_enc}")
P()
P("=" * 60)
P("MODULE 4: SpeechRecognition")
P("=" * 60)
import speech_recognition as sr
P("  Recognizer:", sr.Recognizer)
P("  Microphone:", sr.Microphone)
P("  recognize_google:", sr.Recognizer().recognize_google)
P()
P("=" * 60)
P("MODULE 5: Wikipedia-API")
P("=" * 60)
import wikipediaapi
w = wikipediaapi.Wikipedia(user_agent="TestBot/1.0 (test@example.com)", language="en")
p = w.page("Python (programming language)")
P("  Page exists:", p.exists())
P("  Title:", p.title)
P("  Summary[:60]:", p.summary[:60])
P()
P("=" * 60)
P("MODULE 6: PyAutoGUI")
P("=" * 60)
import pyautogui
P("  Size:", pyautogui.size())
P("  Position:", pyautogui.position())
P()
P("=" * 60)
P("MODULE 7: language_converter (custom)")
P("=" * 60)
from language_converter import (
    detect_language, is_hindi, is_english, translate_text,
    reply_in_same_language, HINDI_TEMPLATES, LANG_MAP,
)
P("  detect_language('Hello'):", detect_language("Hello"))
P("  detect_language('namaste'):", detect_language("namaste"))
P("  detect_language('Mera assignment ho gaya'):", detect_language("Mera assignment ho gaya"))
P("  is_hindi('namaste'):", is_hindi("namaste"))
P("  is_english('Hello'):", is_english("Hello"))
P("  translate_text('hello','hi'):", translate_text("hello", "hi"))
P("  translate_text('I am fine','hi'):", translate_text("I am fine", "hi"))
P("  reply_in_same_language('Hello','I am fine'):", reply_in_same_language("Hello", "I am fine"))
P("  reply_in_same_language('namaste','I am fine'):", reply_in_same_language("namaste", "I am fine"))
P("  HINDI_TEMPLATES keys:", len(HINDI_TEMPLATES), "templates loaded")
P("  LANG_MAP keys:", len(LANG_MAP), "languages mapped")
P()
P("=" * 60)
P("MODULE 8: assistant.py integration")
P("=" * 60)
import importlib, assistant
importlib.reload(assistant)
P("  assistant imported OK")
P("  engine:", "initialized" if assistant.engine is not None else "None")
P("  LANGUAGE_CONVERTER_AVAILABLE:", assistant.LANGUAGE_CONVERTER_AVAILABLE)
P("  speak() signature accepts user_text:", "user_text" in assistant.speak.__code__.co_varnames)
P("  wishme() exists:", hasattr(assistant, "wishme"))
P("  time() exists:", hasattr(assistant, "time"))
P("  date() exists:", hasattr(assistant, "date"))
P("  tell_joke() exists:", hasattr(assistant, "tell_joke"))
P("  screenshot() exists:", hasattr(assistant, "screenshot"))
P("  takecommand() exists:", hasattr(assistant, "takecommand"))
P()
P("=" * 60)
P("ALL TESTS COMPLETED")
P("=" * 60)
out.close()