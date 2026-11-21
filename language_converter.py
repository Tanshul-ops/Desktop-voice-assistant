"""
Language Converter Module for Voice Assistant
===============================================
Author: Claude Code | Date: 2026-10-15
Purpose: Detect user language (English/Hindi) and reply in same language.
Connects to assistant.py for integrated multilingual experience.
"""

import sys
from pathlib import Path

# Add parent directory to import assistant modules
sys.path.insert(0, str(Path(__file__).parent))

try:
    from langdetect import detect, DetectorFactory
    from langdetect.lang_detect_exception import LangDetectException
    from googletrans import Translator, LANGUAGES
except ImportError as e:
    print("[LanguageConverter] Missing library:", e)
    print("Run: pip install langdetect googletrans==4.0.0-rc1")
    raise

# --- Configuration ---
# Ensure consistent detection results (optional)
DetectorFactory.seed = 42

# Map language codes to human-readable names
LANG_MAP = {
    "en": "English",
    "hi": "Hindi",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "ja": "Japanese",
}

# Initialize once
translator = Translator()


# Common Hindi words/keywords for fallback detection
HINDI_KEYWORDS = [
    "namaste", "kya", "hai", "ho", "kaise", "mera", "aap", "sir",
    "samay", "date", "assignment", "yaad", "mein", "ne", "se",
    "ka", "ki", "ke", "hain", "tha", "bata", "suno",
]

def detect_language(text: str) -> str:
    """
    Detect the language of input text.
    Uses langdetect first; falls back to keyword/script check for Hindi.
    Returns ISO code: 'en', 'hi', etc.
    """
    if not text or not text.strip():
        return "en"
    # Fallback: check for Devanagari script or Hindi keywords
    has_devanagari = any("ऀ" <= c <= "ॿ" for c in text)
    lower_text = text.lower()
    has_hindi_words = any(w in lower_text for w in HINDI_KEYWORDS)
    if has_devanagari or has_hindi_words:
        return "hi"
    try:
        lang = detect(text)
        return lang
    except LangDetectException:
        return "en"


def is_hindi(text: str) -> bool:
    """Quick check if text is likely Hindi."""
    lang = detect_language(text)
    return lang == "hi"


def is_english(text: str) -> bool:
    """Quick check if text is likely English."""
    lang = detect_language(text)
    return lang == "en"


def translate_text(text: str, target: str) -> str:
    """
    Translate text to target language code using googletrans.
    Example: translate_text("hello", "hi") -> "नमस्ते"
    """
    try:
        result = translator.translate(text, dest=target)
        return result.text
    except Exception as e:
        print(f"[Translation Error] {e}")
        return text  # Fallback: return original


def reply_in_same_language(user_text: str, assistant_response_english: str) -> str:
    """
    Main integration function:
    1. Detect language of user_text.
    2. If Hindi -> translate assistant response to Hindi.
    3. If English -> keep as is.
    Returns the final response string.
    """
    user_lang = detect_language(user_text)
    print(f"[SPEAKING] Detected language: {user_lang} ({LANG_MAP.get(user_lang, user_lang)})")

    if user_lang == "hi":
        # User spoke Hindi -> reply in Hindi
        hindi_reply = translate_text(assistant_response_english, "hi")
        return hindi_reply
    elif user_lang == "en":
        # User spoke English -> reply in English
        return assistant_response_english
    else:
        # Other language detected -> try translating response there, else English
        translated = translate_text(assistant_response_english, user_lang)
        return translated


# --- Pre-built Hindi response templates (optional optimization) ---
# These ensure common assistant phrases sound natural in Hindi
HINDI_TEMPLATES = {
    "welcome": "स्वागत है सर!!",
    "good_morning": "सुप्रभात सर!!",
    "good_afternoon": "शुभ दोपहर सर!!",
    "good_evening": "शुभ संध्या सर!!",
    "good_night": "शुभ रात्रि सर, कल मिलते हैं",
    "service": "कुआन आपकी सेवा में, बताइए मैं आपकी कैसे मदद कर सकता हूँ।",
    "time": "वर्तमान समय है",
    "date": "आज की तारीख है",
    "remember": "आपने मुझसे याद रखने को कहा",
    "joke": "मज़ाक सुनिए:",
    "search": "मैं खोज रहा हूँ...",
    "wikipedia": "विकिपीडिया पर खोज रहा हूँ...",
    "screenshot": "स्क्रीनशॉट ले लिया, जांचिए",
    "open_youtube": "YouTube खोल रहा हूँ",
    "play_music": "संगीत चला रहा हूँ",
    "shutdown": "सिस्टम बंद कर रहा हूँ",
    "restart": "सिस्टम पुनः शुरू कर रहा हूँ",
    "lock": "सिस्टम लॉक कर रहा हूँ",
    "sleep": "सिस्टम स्लीप मोड में डाल रहा हूँ",
    "good": "सुनकर अच्छा लगा सर!!",
    "fine": "खुशी हुई सर!!",
    "offline": "बंद कर रहा हूँ",
    "exit": "बाहर निकल रहा हूँ",
    "remember_what": "मैं क्या याद रखूँ?",
    "remember_confirm": "आपने कहा था मैं याद रखूँ:",
    "remember_none": "आपने अभी कुछ याद रखने को नहीं कहा",
    "try_again": "फिर से बोलिए",
    "search_what": "मैं क्या खोजूँ?",
    "chrome_not_found": "Chrome नहीं मिला, डिफ़ॉल्ट ब्राउज़र खोल रहा हूँ",
    "playing_local": "आपकी लाइब्रेरी से संगीत चला रहा हूँ",
    "no_local_music": "स्थानीय संगीत नहीं मिला। YouTube Music खोल रहा हूँ",
}


def get_hindi_template(key: str, fallback_english: str) -> str:
    """
    Get pre-translated Hindi phrase. If not found, translate fallback.
    """
    if key in HINDI_TEMPLATES:
        return HINDI_TEMPLATES[key]
    return translate_text(fallback_english, "hi")


# --- Integration Example ---
if __name__ == "__main__":
    # Demo mode: show how it works
    samples = [
        "Hello, how are you?",
        "नमस्ते, आप कैसे हैं?",
        "what time is it",
        "समय क्या हुआ है",
        "remember that meeting at 3pm",
        "मैंने मीटिंग को याद रख लिया",
    ]

    print("=" * 60)
    print("Language Converter Demo")
    print("=" * 60)

    for s in samples:
        lang = detect_language(s)
        name = LANG_MAP.get(lang, lang)
        # Example: assistant wants to say "I'm fine sir, What about you?"
        assistant_text = "I'm fine sir, What about you?"
        reply = reply_in_same_language(s, assistant_text)
        # Safe print: some terminals (cp1252) can't render non-ASCII
        try:
            print(f"\nUser ({name}): {s}")
            print(f"Detected Code: {lang}")
            print(f"Assistant Reply: {reply}")
        except UnicodeEncodeError:
            print(f"\nUser ({name}): {s.encode('ascii', 'replace')}")
            print(f"Detected Code: {lang}")
            print(f"Assistant Reply: {reply.encode('ascii', 'replace')}")

    print("\n" + "=" * 60)
    print("Demo Complete. Module ready to connect with assistant.py")
