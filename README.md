# 🧠 PDF Content Analysis and Question Viewer

A Python + Flask application to extract and visualize educational PDF content — including text, questions, and options with image grouping. Originally designed for Olympiad-style question papers.

---

## 🚀 Features

- ✅ Extracts all **text** from multi-page educational PDFs
- 🖼️ Extracts and saves **images** from diagrams, patterns, clocks, etc.
- 📂 Groups images as **Question + Options**
- 📊 Generates a **structured JSON** for use with AI/NLP pipelines
- 🌐 View everything in a responsive **Flask web interface**

---

## 📁 Folder Structure

PDF-Content-Analysis/
├── sample.pdf # Input PDF file
├── main.py # Script: extract text + images + JSON
├── structured_output.json # Output: AI-friendly question format
├── app.py # Flask web app
├── static/
│ └── output_images/ # Extracted question/option images
├── templates/
│ └── index.html # Web UI template
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/venkatasai-03/PDF-Content-Analysis.git
cd PDF-Content-Analysis

python -m venv venv
venv\Scripts\activate      # On Windows


#Reqirements

pip install pymupdf flask

#To run
python main.py
