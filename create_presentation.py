"""
Create PowerPoint presentation for AI Desktop Voice Assistant Project
Title Structure: Problem, Aim/Objective, Literature Survey, Technical Details, References, Future Work
"""

from pptx import Presentation
from pptx.util import Inches, Pt

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# ============================================
# SLIDE 1: Problem Statement
# ============================================
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
title.text = "Problem"

content = slide.placeholders[1]
tf = content.text_frame
tf.text = "Users face challenges with:"

p = tf.add_paragraph()
p.text = "• Typing on small devices (mobiles, tablets) is inconvenient"
p.level = 0

p = tf.add_paragraph()
p.text = "• Accessibility issues for physically challenged users"
p.level = 0

p = tf.add_paragraph()
p.text = "• Need for hands-free operation during multitasking"
p.level = 0

p = tf.add_paragraph()
p.text = "• Time-consuming manual navigation and search operations"
p.level = 0

# ============================================
# SLIDE 2: Aim/Objective
# ============================================
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
title.text = "Aim / Objective"

content = slide.placeholders[1]
tf = content.text_frame
tf.text = "To develop a voice-controlled desktop assistant that:"

p = tf.add_paragraph()
p.text = "• Interacts with users through natural voice commands"
p.level = 0

p = tf.add_paragraph()
p.text = "• Performs system tasks hands-free (time, date, jokes)"
p.level = 0

p = tf.add_paragraph()
p.text = "• Searches Wikipedia and retrieves information"
p.level = 0

p = tf.add_paragraph()
p.text = "• Opens websites and applications via voice"
p.level = 0

p = tf.add_paragraph()
p.text = "• Captures screenshots and manages music playback"
p.level = 0

p = tf.add_paragraph()
p.text = "• Provides translation services"
p.level = 0

# ============================================
# SLIDE 3: Literature Survey (Features & Working)
# ============================================
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
title.text = "Literature Survey"

content = slide.placeholders[1]
tf = content.text_frame
tf.text = "Key Features:"

features = [
    "Voice Command Recognition (SpeechRecognition library)",
    "Time & Date Display",
    "Wikipedia Search & Summary",
    "Web Browser Control (YouTube, Google, Stack Overflow)",
    "Music Playback from local directory",
    "Screenshot Capture (pyautogui)",
    "Memory System (save/recall user data)",
    "Text Translation (googletrans library)",
    "Jokes & Entertainment"
]

for feature in features:
    p = tf.add_paragraph()
    p.text = "• " + feature
    p.level = 0

# ============================================
# SLIDE 4: Technical Details (Hardware & Software)
# ============================================
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
title.text = "Technical Details"

content = slide.placeholders[1]
tf = content.text_frame
tf.text = "Hardware Requirements:"

p = tf.add_paragraph()
p.text = "• PC/Laptop with Windows OS"
p.level = 0

p = tf.add_paragraph()
p.text = "• Microphone for voice input"
p.level = 0

p = tf.add_paragraph()
p.text = "• Speakers/Headphones for voice output"
p.level = 0

p = tf.add_paragraph()
p.text = "\nSoftware Requirements:"

p = tf.add_paragraph()
p.text = "• Python 3.6+"
p.level = 0

p = tf.add_paragraph()
p.text = "• pyttsx3 (Text-to-Speech)"
p.level = 0

p = tf.add_paragraph()
p.text = "• SpeechRecognition"
p.level = 0

p = tf.add_paragraph()
p.text = "• wikipediaapi"
p.level = 0

p = tf.add_paragraph()
p.text = "• googletrans"
p.level = 0

p = tf.add_paragraph()
p.text = "• pyautogui, webbrowser, random, datetime"
p.level = 0

# ============================================
# SLIDE 5: References & Future Work
# ============================================
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
title.text = "References & Future Enhancements"

content = slide.placeholders[1]
tf = content.text_frame
tf.text = "References:"

p = tf.add_paragraph()
p.text = "• GitHub: Desktop voice assistant project"
p.level = 0

p = tf.add_paragraph()
p.text = "• Libraries: pyttsx3, SpeechRecognition, wikipediaapi, googletrans"
p.level = 0

p = tf.add_paragraph()
p.text = "\nFuture Work Ideas:"
p.level = 0

future_features = [
    "Weather API integration",
    "News headlines fetcher",
    "Voice calculator",
    "Email sender via voice",
    "System monitor (CPU/RAM/battery)",
    "Timer & stopwatch functions",
    "Note taking & file search",
    "ChatGPT / AI integration",
    "Currency converter",
    "Spotify music control"
]

for feature in future_features:
    p = tf.add_paragraph()
    p.text = "• " + feature
    p.level = 0

# Save to Desktop
desktop_path = "C:/Users/agent/Desktop/AI_Desktop_Voice_Assistant_5_Slides.pptx"
prs.save(desktop_path)
print(f"Presentation updated with future work: {desktop_path}")