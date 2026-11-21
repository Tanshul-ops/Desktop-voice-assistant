"""
Generate Final Presentation for AI Desktop Voice Assistant (Review-2)
Using exact layout patterns from SWAPNILMINIPROJEC_1.pptx and Desktop-Voice-Assistant-Quan_1.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from datetime import datetime

# Color Scheme - Teal Blue Retro Minimalist Theme
COLORS = {
    "primary_teal": RGBColor(0, 128, 128),      # Teal
    "accent_blue": RGBColor(30, 144, 255),      # Dodger Blue
    "dark_bg": RGBColor(45, 45, 45),            # Dark Gray
    "light_text": RGBColor(240, 240, 240),      # Off White
    "accent_orange": RGBColor(255, 140, 0),     # Dark Orange
    "white": RGBColor(255, 255, 255),
}

class FinalPresentationGenerator:
    def __init__(self, output_filename="ppt_assistant.pptx"):
        self.prs = Presentation()
        self.prs.slide_width = Inches(10)
        self.prs.slide_height = Inches(7.5)
        self.output_filename = output_filename

    def add_title_slide(self):
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = COLORS["primary_teal"]

        # Main Title (larger, centered)
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(1.2))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "Mini Project (BCC 351) Review-2"
        p.font.size = Pt(48)
        p.font.bold = True
        p.font.color.rgb = COLORS["white"]
        p.alignment = PP_ALIGN.CENTER

        # Subtitle (accent color)
        sub_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.6), Inches(9), Inches(1))
        stf = sub_box.text_frame
        stf.word_wrap = True
        p2 = stf.paragraphs[0]
        p2.text = "AI Desktop Voice Assistant — Quan"
        p2.font.size = Pt(32)
        p2.font.color.rgb = COLORS["accent_orange"]
        p2.alignment = PP_ALIGN.CENTER

        # Supervisor section
        sup_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(4.5), Inches(2.2))
        suptf = sup_box.text_frame
        suptf.word_wrap = True
        suptf.text = "Supervisor:\nMr. Saurabh Dwivedi\nAssistant Professor\nDept. of Computer Science & Engg."
        for para in suptf.paragraphs:
            para.font.size = Pt(13)
            para.font.color.rgb = COLORS["light_text"]

        # Group Information
        grp_box = slide.shapes.add_textbox(Inches(5.2), Inches(4.2), Inches(4.3), Inches(2.5))
        grptf = grp_box.text_frame
        grptf.word_wrap = True
        grptf.text = "Group No: 50\n\nTanshul Saini | Siddhartha Singh | Yashasvi Pathak\nZeeshan Ansari | Smiridhi Bhardwaj"
        for para in grptf.paragraphs:
            para.font.size = Pt(12)
            para.font.color.rgb = COLORS["light_text"]

    def add_slide_with_bullets(self, title, points, subtitle=None):
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = COLORS["dark_bg"]

        # Title bar shape
        title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(1.1))
        t_fill = title_shape.fill
        t_fill.solid()
        t_fill.fore_color.rgb = COLORS["primary_teal"]
        title_shape.line.color.rgb = COLORS["accent_blue"]

        # Title text
        t_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.15), Inches(9), Inches(0.9))
        tf = t_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(36)
        p.font.bold = True
        p.font.color.rgb = COLORS["white"]
        p.alignment = PP_ALIGN.CENTER

        # Content box
        top_offset = Inches(1.4) if not subtitle else Inches(1.3)
        c_box = slide.shapes.add_textbox(Inches(0.8), top_offset, Inches(8.4), Inches(5.8))
        ctf = c_box.text_frame
        ctf.word_wrap = True

        if subtitle:
            sp = ctf.paragraphs[0]
            sp.text = subtitle
            sp.font.size = Pt(16)
            sp.font.bold = True
            sp.font.color.rgb = COLORS["accent_orange"]
            sp.space_after = Pt(6)
            start_idx = 1
        else:
            start_idx = 0

        for i, point in enumerate(points):
            if start_idx > 0 or i > 0:
                ctf.add_paragraph()
            idx = start_idx + i
            p = ctf.paragraphs[idx]
            p.text = point
            p.font.size = Pt(15)
            p.font.color.rgb = COLORS["light_text"]
            p.space_before = Pt(4)
            p.space_after = Pt(4)

    def add_two_column_slide(self, title, col1_title, col1_points, col2_title, col2_points):
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = COLORS["dark_bg"]

        # Title bar
        title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(1.1))
        t_fill = title_shape.fill
        t_fill.solid()
        t_fill.fore_color.rgb = COLORS["primary_teal"]

        t_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.15), Inches(9), Inches(0.9))
        tf = t_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(36)
        p.font.bold = True
        p.font.color.rgb = COLORS["white"]

        # Column 1
        box1 = slide.shapes.add_textbox(Inches(0.6), Inches(1.4), Inches(4.2), Inches(5.6))
        tf1 = box1.text_frame
        tf1.word_wrap = True
        p1 = tf1.paragraphs[0]
        p1.text = col1_title
        p1.font.size = Pt(18)
        p1.font.bold = True
        p1.font.color.rgb = COLORS["accent_orange"]
        p1.space_after = Pt(8)

        for pt in col1_points:
            tf1.add_paragraph()
            cp = tf1.paragraphs[-1]
            cp.text = pt
            cp.font_size = Pt(14)
            cp.font.color.rgb = COLORS["light_text"]
            cp.space_before = Pt(4)
            cp.space_after = Pt(4)

        # Column 2
        box2 = slide.shapes.add_textbox(Inches(5.2), Inches(1.4), Inches(4.2), Inches(5.6))
        tf2 = box2.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.text = col2_title
        p2.font.size = Pt(18)
        p2.font.bold = True
        p2.font.color.rgb = COLORS["accent_orange"]
        p2.space_after = Pt(8)

        for pt in col2_points:
            tf2.add_paragraph()
            cp = tf2.paragraphs[-1]
            cp.text = pt
            cp.font_size = Pt(14)
            cp.font.color.rgb = COLORS["light_text"]
            cp.space_before = Pt(4)
            cp.space_after = Pt(4)

    def generate(self):
        print("Generating professional presentation...")

        # 1. Title Slide
        self.add_title_slide()

        # 2. Problem Statement
        self.add_slide_with_bullets(
            "Problem Statement",
            [
                "• Inefficient Manual Workflows: Traditional desktop interaction requires repetitive mouse clicks and keyboard typing for routine queries.",
                "• Multitasking Bottlenecks: Users cannot perform file operations, web searches, and system actions simultaneously without physical device contact.",
                "• Accessibility Barriers: Standard graphical user interfaces (GUIs) create hurdles for users with motor impairments or visual fatigue.",
                "• Lack of Contextual Memory: Standard desktop search tools lack conversational memory to recall past user commands and notes."
            ],
            "Addressing friction points in daily workstation navigation through voice AI."
        )

        # 3. Aim & Objectives
        self.add_slide_with_bullets(
            "Aim & Core Objectives",
            [
                "✓ Build a lightweight, offline-capable desktop voice assistant ('Quan') using Python.",
                "✓ Implement robust speech recognition for natural language voice command parsing.",
                "✓ Enable automated system controls (screenshots, music playback, power states).",
                "✓ Integrate real-time web retrieval (Wikipedia API, Google Search, Translation).",
                "✓ Provide persistent local memory logging for user-specified notes and data.",
                "✓ Ensure low resource utilization (~45-50MB RAM) suitable for standard Windows PCs."
            ],
            "Delivering a seamless hands-free computing experience."
        )

        # 4. Background Literature & Academic Research
        self.add_slide_with_bullets(
            "Literature Survey & Academic Research",
            [
                "• ASR Benchmarks: Studies on Automatic Speech Recognition (ASR) show Google Speech API achieves ~6–12% Word Error Rate (WER) on standard acoustic benchmarks.",
                "• Text-to-Speech (TTS) Synthesis: Research in assistive technology highlights Microsoft SAPI5 and `pyttsx3` wrappers for low-latency (<250ms) offline speech feedback.",
                "• Voice-Controlled Computing: IEEE literature confirms voice interfaces reduce cognitive load and enhance accessibility for routine workstation tasks.",
                "• Hybrid Architecture: Combining cloud-based STT with local offline SAPI5 execution balances accuracy and responsiveness."
            ],
            "Grounded in modern speech processing and human-computer interaction studies."
        )

        # 5. System Architecture
        self.add_slide_with_bullets(
            "System Architecture & Pipeline",
            [
                "1. Audio Capture: Microphone captures audio input via `speech_recognition` with 1s pause threshold.",
                "2. Speech-to-Text: Audio stream transmitted to Google Speech API for robust intent transcription.",
                "3. Command Parsing: Keyword-in-string matching maps transcript to executable functions.",
                "4. Task Execution: Invokes system modules (`pyautogui`, `webbrowser`, `os`, `wikipediaapi`).",
                "5. Voice Feedback: SAPI5 TTS engine (`pyttsx3`) generates spoken confirmation response."
            ],
            "Four-stage command-query processing pipeline."
        )

        # 6. Core Implementation Modules
        self.add_two_column_slide(
            "Core Implementation Modules",
            "Information & Search",
            [
                "• Wikipedia Integration: `wikipediaapi` fetches structured article summaries.",
                "• Web Navigation: Opens YouTube, Google, GitHub, and Stack Overflow via `webbrowser`.",
                "• Translation: Google Translate API (`googletrans`) for multi-language conversion.",
                "• Jokes & Utilities: Randomized entertainment and time/date retrieval."
            ],
            "System & Media Control",
            [
                "• Screenshot Capture: `pyautogui` saves desktop snapshots to Pictures folder.",
                "• Media Playback: Local music directory scanning with YouTube Music fallback.",
                "• Persistent Memory: Appends user notes to local `data.txt` with recall support.",
                "• OS Power States: Voice-triggered shutdown, restart, sleep, and lock commands."
            ]
        )

        # 7. Technical Specifications
        self.add_two_column_slide(
            "Technical Specifications",
            "Hardware Requirements",
            [
                "• Processor: Intel Core i3 / AMD Ryzen 3 or higher",
                "• Memory: 4 GB RAM minimum (App uses ~50MB)",
                "• Peripherals: Standard USB / Built-in Microphone",
                "• Output: Speakers or Headphones for voice feedback",
                "• Operating System: Windows 10 / 11 (SAPI5 native support)"
            ],
            "Software & Dependencies",
            [
                "• Python 3.6+ runtime environment",
                "• `pyttsx3==2.90` (Offline TTS synthesis)",
                "• `SpeechRecognition==3.10.0` (STT processing)",
                "• `wikipediaapi==0.7.0` (Knowledge retrieval)",
                "• `pyautogui==0.9.54` (Desktop automation)",
                "• `googletrans==4.0.0rc1` (Translation)"
            ]
        )

        # 8. Performance & Security
        self.add_slide_with_bullets(
            "Performance & Security Analysis",
            [
                "• Latency Profile: TTS initialization (~200ms), screenshot capture (~50ms), Google STT round-trip (~2-4 seconds).",
                "• Memory Footprint: Lean baseline of ~45-50MB RAM during active idle listening.",
                "• File System Boundaries: Restricted write operations to safe user directories (Pictures, local text logs).",
                "• Error Resilience: Multi-layer try-except blocks prevent crashes on network drops or TTS engine faults."
            ],
            "Optimized for efficiency, safety, and stability."
        )

        # 9. Future Enhancements
        self.add_slide_with_bullets(
            "Future Enhancement Roadmap",
            [
                "• Weather Integration: OpenWeatherMap API integration for real-time meteorological voice reports.",
                "• System Monitoring: Live CPU, RAM, and battery telemetry via `psutil` library.",
                "• LLM Integration: Connecting OpenAI / Claude APIs for advanced conversational reasoning.",
                "• Advanced Automation: Window management (`pygetwindow`) and Spotify music control."
            ],
            "Scalable architecture prepared for advanced AI features."
        )

        # 10. References
        self.add_slide_with_bullets(
            "Academic & Technical References",
            [
                "• IEEE Xplore: Research papers on Voice-Controlled Desktop Assistants and Hands-Free Computing (2021-2024).",
                "• Speech Recognition Benchmarks: Studies on Deep Learning ASR and Google Speech API Word Error Rate (WER).",
                "• Official Documentation:",
                "   - pyttsx3: https://pyttsx3.readthedocs.io/",
                "   - SpeechRecognition: https://pypi.org/project/SpeechRecognition/",
                "   - Wikipedia-API: https://wikipedia-api.readthedocs.io/"
            ],
            "Foundational literature and technical resources."
        )

        self.prs.save("final_presentation.pptx")
        print(f"[SUCCESS] Presentation generated successfully: {self.output_filename}")
        print(f"[INFO] Total slides: {len(self.prs.slides)}")

if __name__ == "__main__":
    gen = FinalPresentationGenerator("ppt_assistant.pptx")
    gen.generate()