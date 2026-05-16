import ollama

def generate_flashcards(text):

    prompt = f"""
    You are an AI study assistant.
    
    Create concise flashcards from the notes below.
    
    Rules:
    - Keep answers under 20 words
    - One concept per flashcard
    - Use simple student-friendly language
    - Format exactly like this:
    
    Q: Question
    A: Answer
    
    Generate 10 flashcards.
    
    Notes:
    {text[:4000]}
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]