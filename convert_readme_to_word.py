#!/usr/bin/env python3
"""
README to Word Document Converter
Converts the README.md file to a professional Word document
"""

import re
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
import os

def create_word_document():
    """Convert README.md to a Word document"""

    # Read the README file
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create a new Word document
    doc = Document()

    # Set document properties
    doc.core_properties.title = "Simple Groq Chatbot Documentation"
    doc.core_properties.author = "Muhammad Maheem"
    doc.core_properties.subject = "Flask Chatbot Application Documentation"

    # Add title
    title = doc.add_heading('Simple Groq Chatbot', 0)
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    # Add subtitle
    subtitle = doc.add_paragraph()
    subtitle.add_run('AI Chatbot Application Documentation').bold = True
    subtitle.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    # Split content by lines
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Skip the first title line (already added)
        if line.startswith('# Simple Groq Chatbot'):
            i += 1
            continue

        # Handle headers
        if line.startswith('## '):
            doc.add_heading(line[3:], 1)
        elif line.startswith('### '):
            doc.add_heading(line[4:], 2)
        elif line.startswith('#### '):
            doc.add_heading(line[5:], 3)

        # Handle bullet points
        elif line.startswith('- ') or line.startswith('* '):
            bullet_text = line[2:]
            # Handle bold text in bullet points
            bullet_para = doc.add_paragraph(style='List Bullet')
            add_formatted_text(bullet_para, bullet_text)

        # Handle numbered lists
        elif re.match(r'^\d+\.\s', line):
            list_text = re.sub(r'^\d+\.\s', '', line)
            list_para = doc.add_paragraph(style='List Number')
            add_formatted_text(list_para, list_text)

        # Handle code blocks
        elif line.startswith('```'):
            # Find the end of the code block
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1

            if code_lines:
                code_para = doc.add_paragraph()
                code_run = code_para.add_run('\n'.join(code_lines))
                code_run.font.name = 'Courier New'
                code_run.font.size = Pt(10)
                # Add light gray background (simulated with border)
                code_para.paragraph_format.left_indent = Inches(0.25)
                code_para.paragraph_format.right_indent = Inches(0.25)

        # Handle regular paragraphs
        elif line and not line.startswith('#') and not line.startswith('```'):
            para = doc.add_paragraph()
            add_formatted_text(para, line)

        i += 1

    # Save the document
    output_path = os.path.join(os.path.dirname(__file__), 'README_Documentation.docx')
    doc.save(output_path)
    print(f"Word document created successfully: {output_path}")
    return output_path

def add_formatted_text(paragraph, text):
    """Add text with formatting (bold, italic) to a paragraph"""

    # Split text by markdown formatting
    parts = re.split(r'(\*\*.*?\*\*|\*.*?\*)', text)

    for part in parts:
        if not part:
            continue

        run = paragraph.add_run()

        if part.startswith('**') and part.endswith('**'):
            # Bold text
            run.add_text(part[2:-2])
            run.bold = True
        elif part.startswith('*') and part.endswith('*'):
            # Italic text
            run.add_text(part[1:-1])
            run.italic = True
        else:
            # Regular text
            run.add_text(part)

if __name__ == '__main__':
    create_word_document()