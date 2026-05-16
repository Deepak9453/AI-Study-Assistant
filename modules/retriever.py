import ollama

def ask_question(vectorstore, question):

    docs = vectorstore.similarity_search(question, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]