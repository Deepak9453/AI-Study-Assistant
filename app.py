import streamlit as st
from modules.pdf_loader import load_pdf
from modules.chunking import split_text
from modules.embeddings import create_vectorstore
from modules.retriever import ask_question
from modules.quiz_generator import generate_quiz
from modules.flashcards import generate_flashcards
from modules.summarizer import summarize_notes

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Study Assistant",
    layout="wide",
    page_icon="📚"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #F5F7FB;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #111827;
}

.stTextInput > div > div > input {
    border-radius: 12px;
    padding: 10px;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    font-size: 16px;
    font-weight: bold;
    background-color: #4F46E5;
    color: white;
}

.stButton > button:hover {
    background-color: #6366F1;
    color: white;
}

.custom-card {
    background-color: white;
    padding: 25px;
    border-radius: 16px;
    margin-top: 15px;
    margin-bottom: 15px;
    border: 1px solid #E5E7EB;
    color: #111827;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.custom-card p {
    color: #111827;
    font-size: 16px;
    line-height: 1.8;
}

.custom-card h4 {
    color: #4F46E5;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.title("📚 AI Study Assistant")
st.caption("Learn smarter with AI-powered summaries, quizzes, flashcards, and doubt solving.")

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.header("⚙️ Settings")

    uploaded_file = st.file_uploader(
        "Upload Study PDF",
        type="pdf"
    )

    st.markdown("---")

    st.info("""
    ### Features
    ✅ Ask Questions  
    ✅ Quiz Generator  
    ✅ Flashcards  
    ✅ Summarizer  
    """)

# ---------------- PDF PROCESSING ---------------- #

if uploaded_file:

    with st.spinner("📄 Processing PDF..."):
        text = load_pdf(uploaded_file)
        chunks = split_text(text)
        vectorstore = create_vectorstore(chunks)

    st.success("✅ PDF Processed Successfully!")

    # ---------------- METRICS ---------------- #

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Chunks Created", len(chunks))

    with col2:
        st.metric("Characters", len(text))

    with col3:
        st.metric("AI Model", "Llama3")

    st.markdown("---")

    # ---------------- TABS ---------------- #

    tab1, tab2, tab3, tab4 = st.tabs([
        "💬 Ask Doubts",
        "📝 Quiz",
        "🧠 Flashcards",
        "📘 Summary"
    ])

    # ---------------- ASK QUESTIONS ---------------- #

    with tab1:

        st.subheader("💬 Ask Questions from Notes")

        question = st.chat_input("Ask your doubt...")

        if question:

            with st.chat_message("user"):
                st.write(question)

            with st.spinner("🤖 Thinking..."):
                response = ask_question(vectorstore, question)

            with st.chat_message("assistant"):
                st.write(response)

    # ---------------- QUIZ ---------------- #

    with tab2:

        st.subheader("📝 AI Quiz Generator")

        if st.button("Generate Quiz"):

            with st.spinner("Generating Quiz..."):

                quiz = generate_quiz(text)

            st.markdown(f"""
            <div class="custom-card">
            <h4>Generated Quiz</h4>
            <p>{quiz}</p>
            </div>
            """, unsafe_allow_html=True)

    # ---------------- FLASHCARDS ---------------- #

    with tab3:

        st.subheader("🧠 Smart Flashcards")

        if st.button("Generate Flashcards"):

            with st.spinner("Creating Flashcards..."):

                flashcards = generate_flashcards(text)

            st.markdown(f"""
            <div class="custom-card">
            <h4>Flashcards</h4>
            <p>{flashcards}</p>
            </div>
            """, unsafe_allow_html=True)

    # ---------------- SUMMARY ---------------- #

    with tab4:

        st.subheader("📘 Chapter Summary")

        if st.button("Generate Summary"):

            with st.spinner("Summarizing Notes..."):

                summary = summarize_notes(text)

            st.markdown(f"""
            <div class="custom-card">
            <h4>Summary</h4>
            <p>{summary}</p>
            </div>
            """, unsafe_allow_html=True)

else:

    st.info("⬅️ Upload a PDF from the sidebar to get started.")