"""
PPT Assistant - Presentation Generator for Voice Assistant Project
Based on: Teal Blue Retro Minimalist Group Project Presentation
Data Source: ttdeaskptop.pptx

This module creates professional presentations programmatically using the extracted
data from the voice assistant project presentation.
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

class PPTAssistant:
    """Main class to generate presentation slides for the voice assistant project."""

    def __init__(self, output_filename="ppt_assistant.pptx"):
        """Initialize the presentation with default settings."""
        self.prs = Presentation()
        self.prs.slide_width = Inches(10)
        self.prs.slide_height = Inches(7.5)
        self.output_filename = output_filename

    def add_title_slide(self):
        """Add the title slide with project information."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])  # Blank layout
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = COLORS["primary_teal"]

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(1))
        title_frame = title_box.text_frame
        title_frame.text = "Mini Project (BCC 351) Presentation"
        title_para = title_frame.paragraphs[0]
        title_para.font.size = Pt(54)
        title_para.font.bold = True
        title_para.font.color.rgb = COLORS["white"]
        title_para.alignment = PP_ALIGN.CENTER

        # Subtitle
        subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.8), Inches(9), Inches(1))
        subtitle_frame = subtitle_box.text_frame
        subtitle_frame.text = "Desktop Voice Assistant (Quan)"
        subtitle_para = subtitle_frame.paragraphs[0]
        subtitle_para.font.size = Pt(36)
        subtitle_para.font.color.rgb = COLORS["accent_orange"]
        subtitle_para.alignment = PP_ALIGN.CENTER

        # Supervisor
        supervisor_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(4.5), Inches(1.5))
        supervisor_frame = supervisor_box.text_frame
        supervisor_frame.word_wrap = True
        supervisor_frame.text = "Supervisor:\nMr. Saurabh Dwivedi\nAssistant Professor\nDept. of CSE"
        for para in supervisor_frame.paragraphs:
            para.font.size = Pt(14)
            para.font.color.rgb = COLORS["light_text"]

        # Group Information
        group_box = slide.shapes.add_textbox(Inches(5.5), Inches(4.2), Inches(4), Inches(2))
        group_frame = group_box.text_frame
        group_frame.word_wrap = True
        group_frame.text = "Group No: 50\n\nTanshul Saini\nSiddhartha Singh\nYashasvi Pathak\nZeeshan Ansari\nSmiridhi Bhardwaj"
        for para in group_frame.paragraphs:
            para.font.size = Pt(12)
            para.font.color.rgb = COLORS["light_text"]

    def add_content_slide(self, title, content_points):
        """Add a content slide with title and bullet points."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])  # Blank layout

        # Background
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = COLORS["dark_bg"]

        # Add title bar
        title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(1.2))
        title_fill = title_shape.fill
        title_fill.solid()
        title_fill.fore_color.rgb = COLORS["primary_teal"]
        title_shape.line.color.rgb = COLORS["accent_blue"]

        # Title text
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(9), Inches(1))
        title_frame = title_box.text_frame
        title_frame.text = title
        title_para = title_frame.paragraphs[0]
        title_para.font.size = Pt(44)
        title_para.font.bold = True
        title_para.font.color.rgb = COLORS["white"]

        # Content
        content_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(8.4), Inches(5.5))
        text_frame = content_box.text_frame
        text_frame.word_wrap = True

        for i, point in enumerate(content_points):
            if i > 0:
                text_frame.add_paragraph()
            p = text_frame.paragraphs[i]
            p.text = point
            p.font.size = Pt(18)
            p.font.color.rgb = COLORS["light_text"]
            p.space_before = Pt(8)
            p.space_after = Pt(8)
            p.level = 0

    def add_problem_slide(self):
        """Add the Problem slide."""
        problems = [
            "• Inefficient Manual Input: Typing and navigating manually on small screens is slow and error-prone.",
            "• Limited Multitasking: Performing tasks requires constant physical interaction, preventing hands-free operation.",
            "• Accessibility Barriers: Traditional UI interactions exclude users with physical disabilities or motor impairments.",
            "• Frictional Navigation: Executing routine searches and app-switching requires repetitive, time-consuming steps."
        ]
        self.add_content_slide("Problem", problems)

    def add_objective_slide(self):
        """Add the Aim/Objective slide."""
        objectives = [
            "✓ Interacts with users through natural voice commands",
            "✓ Performs system tasks hands-free (time, date, jokes)",
            "✓ Searches Wikipedia and retrieves information",
            "✓ Opens websites and applications via voice",
            "✓ Captures screenshots and manages music playback",
            "✓ Provides translation services"
        ]
        self.add_content_slide("Aim / Objective", objectives)

    def add_literature_slide(self):
        """Add the Literature Survey slide."""
        features = [
            "• Voice Command Recognition (SpeechRecognition library)",
            "• Time & Date Display",
            "• Wikipedia Search & Summary",
            "• Web Browser Control (YouTube, Google, Instagram, Github)",
            "• Music Playback from local directory",
            "• Screenshot Capture (pyautogui)",
            "• Memory System (save/recall user data)",
            "• Text Translation (googletrans library)",
            "• Jokes & Entertainment"
        ]
        self.add_content_slide("Literature Survey", features)

    def add_technical_slide(self):
        """Add the Technical Details slide."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = COLORS["dark_bg"]

        # Title bar
        title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(1.2))
        title_fill = title_shape.fill
        title_fill.solid()
        title_fill.fore_color.rgb = COLORS["primary_teal"]

        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(9), Inches(1))
        title_frame = title_box.text_frame
        title_frame.text = "Technical Details"
        title_para = title_frame.paragraphs[0]
        title_para.font.size = Pt(44)
        title_para.font.bold = True
        title_para.font.color.rgb = COLORS["white"]

        # Hardware Section
        hw_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(4.2), Inches(5.5))
        hw_frame = hw_box.text_frame
        hw_frame.word_wrap = True
        hw_frame.text = "Hardware Requirements:\n• PC/Laptop with Windows OS\n• Microphone for voice input\n• Speakers/Headphones for voice output"
        hw_frame.paragraphs[0].font.size = Pt(16)
        hw_frame.paragraphs[0].font.bold = True
        hw_frame.paragraphs[0].font.color.rgb = COLORS["accent_orange"]
        for para in hw_frame.paragraphs[1:]:
            para.font.size = Pt(14)
            para.font.color.rgb = COLORS["light_text"]

        # Software Section
        sw_box = slide.shapes.add_textbox(Inches(5.2), Inches(1.5), Inches(4.2), Inches(5.5))
        sw_frame = sw_box.text_frame
        sw_frame.word_wrap = True
        sw_frame.text = "Software Requirements:\n• Python 3.6+\n• pyttsx3 (Text-to-Speech)\n• SpeechRecognition\n• wikipediaapi\n• googletrans\n• pyautogui, webbrowser"
        sw_frame.paragraphs[0].font.size = Pt(16)
        sw_frame.paragraphs[0].font.bold = True
        sw_frame.paragraphs[0].font.color.rgb = COLORS["accent_orange"]
        for para in sw_frame.paragraphs[1:]:
            para.font.size = Pt(14)
            para.font.color.rgb = COLORS["light_text"]

    def add_references_slide(self):
        """Add the References slide."""
        references = [
            "GitHub Repositories:",
            "• python-speech-recognition",
            "• Wikipedia-API by martin-majlis",
            "",
            "AI Models & Technologies:",
            "• Google Speech Recognition API",
            "• Google Translate API",
            "• Wikipedia API (wikipediaapi)",
            "",
            "Documentation:",
            "• pyttsx3: https://pyttsx3.readthedocs.io/",
            "• SpeechRecognition: https://pypi.org/project/SpeechRecognition/"
        ]
        self.add_content_slide("References", references)

    def create_presentation(self):
        """Create the complete presentation with all slides."""
        print("Creating presentation...")
        self.add_title_slide()
        self.add_problem_slide()
        self.add_objective_slide()
        self.add_literature_slide()
        self.add_technical_slide()
        self.add_references_slide()

        # Save presentation
        self.prs.save(self.output_filename)
        print(f"[OK] Presentation created successfully: {self.output_filename}")
        print(f"[OK] Total slides: {len(self.prs.slides)}")
        print(f"[OK] Saved at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    """Main function to generate the presentation."""
    assistant = PPTAssistant("ppt_assistant.pptx")
    assistant.create_presentation()


if __name__ == "__main__":
    main()
