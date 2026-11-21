"""
Audio test script to diagnose speaker output issues.
Run this separately: python audio_test.py
"""

import sys
import pyttsx3
import winsound

def test_basic_audio():
    """Test if basic Windows audio works."""
    print("=== Testing Basic Windows Audio ===")
    try:
        print("Playing system beep (2000Hz for 200ms)...")
        winsound.Beep(2000, 200)
        print("System beep played successfully!")
        return True
    except Exception as e:
        print(f"System beep failed: {e}")
        return False

def test_pyttsx3():
    """Test pyttsx3 engine thoroughly."""
    print("\n=== Testing pyttsx3 Engine ===")

    print("Initializing engine...")
    engine = pyttsx3.init()

    # Get all properties
    voices = engine.getProperty('voices')
    print(f"Found {len(voices)} voice(s):")
    for i, v in enumerate(voices):
        print(f"  {i}: {v.name}")

    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    print(f"Rate: {rate} | Volume: {volume}")

    # Set to known good values
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    # Test each voice
    for i, v in enumerate(voices):
        print(f"\nTesting voice {i}: {v.name}")
        engine.setProperty('voice', v.id)
        engine.say(f"Testing voice number {i}, this is {v.name}")
        engine.runAndWait()

    print("\npyttsx3 test complete!")

def test_say_short():
    """Test with a very short phrase to check timing."""
    print("\n=== Testing Short Phrase ===")
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 150)

    print("Speaking: 'Hello'")
    engine.say("Hello")
    engine.runAndWait()
    print("Done")

def main():
    print("=" * 50)
    print("Voice Assistant Audio Diagnostic Test")
    print("=" * 50)

    # Test 1: Basic Windows audio
    basic_works = test_basic_audio()

    # Test 2: Very short phrase
    test_say_short()

    # Test 3: Full pyttsx3 test
    test_pyttsx3()

    print("\n" + "=" * 50)
    print("DIAGNOSTIC RESULTS:")
    print("=" * 50)

    if basic_works:
        print("- Windows audio system: WORKING")
    else:
        print("- Windows audio system: FAILED (check speakers/volume)")

    print("\nIf Windows audio beep works but pyttsx3 doesn't:")
    print("1. Check if pyttsx3 is using SAPI5 driver correctly")
    print("2. Try running as administrator")
    print("3. Check Windows Sound Control Panel > Sound > Playback")

if __name__ == "__main__":
    main()