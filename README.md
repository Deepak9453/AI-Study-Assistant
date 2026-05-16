📚 AI Study Assistant

AI Study Assistant is an AI-powered EdTech application that helps students learn smarter from their study materials.

The application allows students to:

Upload study PDFs
Ask questions from notes
Generate quizzes automatically
Create flashcards
Summarize chapters

The project uses Retrieval-Augmented Generation (RAG) with Llama3 via Ollama to provide intelligent and context-aware responses.

🚀 Features

✅ PDF Upload & Processing
✅ AI Doubt Solving
✅ Automatic Quiz Generation
✅ Smart Flashcards
✅ AI Summarization
✅ Local LLM using Ollama + Llama3
✅ Modern Streamlit UI
✅ RAG-based Context Retrieval

# 📸 Screenshots

## Home Page

![Home](screenshots/pic1.png)

---

## Quiz Generator

![Quiz](screenshots/pic2.png)

---

## Flashcards

![Flashcards](screenshots/pic3.png)

---

## Summary Feature

![Summary](screenshots/pic5.png)

🛠️ Tech Stack
Frontend
Streamlit
Backend / AI
Python
LangChain
Ollama
Llama3
Vector Database
FAISS
Embeddings
HuggingFace Sentence Transformers
🧠 Architecture
Student Uploads PDF
        ↓
Text Extraction
        ↓
Chunking
        ↓
Embeddings Creation
        ↓
FAISS Vector Store
        ↓
Similarity Search
        ↓
Relevant Context Retrieval
        ↓
Llama3 via Ollama
        ↓
AI Response / Quiz / Flashcards / Summary
📂 Project Structure
AI_EDU_TECH/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── quiz_generator.py
│   ├── flashcards.py
│   └── summarizer.py
│
├── assets/
└── screenshots/


⚙️ Installation

1. Clone Repository

git clone <your-repo-link>

2. Navigate to Project

cd AI_EDU_TECH

3. Activate Virtual Environment

Windows
.venv\Scripts\activate

📦 Install Dependencies

pip install -r requirements.txt

🤖 Run Ollama

ollama run llama3

▶️ Run Application

streamlit run app.py


🧩 Prompt Engineering

The prompts were carefully designed to:

Generate concise summaries
Create student-friendly flashcards
Generate structured MCQs
Reduce hallucinations
Improve readability

Example:

You are an AI Study Assistant.
Generate concise flashcards from the notes below.
Keep answers short and student-friendly.


⚠️ Challenges Faced

Handling large PDF content
Improving response quality
Reducing hallucinations
Better formatting of flashcards and quizzes
Designing a clean and readable UI
Managing chunking and retrieval accuracy


🔮 Future Improvements

Voice-based learning assistant
Multilingual support
Student progress tracking
Adaptive learning recommendations
Cloud deployment
Authentication system

👨‍💻 Author

Deepak Kumar Prajapati