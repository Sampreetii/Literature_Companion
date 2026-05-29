# 📚 Literature Companion

Literature Companion is an AI-powered reading assistant that helps readers understand classic books written in difficult or old-fashioned English.

Many classic novels have beautiful stories, but translations and older writing styles can make them difficult for modern readers. This project converts classic literature into clear modern English while preserving the author's original meaning, emotion, and atmosphere.

---

## ✨ Features

### 📖 Classic Text Modernization
Transforms difficult literary passages into natural modern English without summarizing or removing important details.

### 🎚️ Reading Styles
Choose how you want to experience the text:

- **Simple** – easier language for comfortable reading
- **Modern** – natural English while preserving style
- **Literary** – keeps more of the original author's voice

### 📚 PDF Support
Upload classic books or passages directly as PDF files.

### 🧠 Reader Notes
Optional explanations including:

- Difficult vocabulary
- Old-fashioned expressions
- Hidden emotional meaning behind passages

### 💡 Literary Understanding
Explains deeper meanings in a friendly way, helping readers understand characters, emotions, and themes.

---

## 🖼️ How It Works

1. Upload a PDF or paste classic literature text.
2. Choose your reading style.
3. The AI rewrites the passage into modern English.
4. Optional notes help explain difficult parts.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini AI
- pypdf

---

## 📂 Project Structure

```
Literature-Companion/

├── app.py
├── utils.py
├── prompts.py
├── pdf_utils.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

Clone the repository:

```bash
git clone https://github.com/Sampreetii/literature_companion.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## 🚀 Future Improvements

- Full book reading mode
- Chapter navigation
- Previous/Next page controls
- Reading progress saving
- AI-generated summaries for completed chapters
- Personalized reading difficulty

---

## ❤️ Motivation

This project was inspired by the challenge many readers face when trying to enjoy classic literature.

Books like *White Nights* by Fyodor Dostoevsky contain beautiful ideas and emotions, but the language can create a barrier.

Literature Companion aims to remove that barrier while keeping the soul of the original work.

---
