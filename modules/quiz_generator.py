import ollama

def generate_quiz(text):

    prompt = f"""
    You are an AI tutor.

Generate 5 high-quality multiple choice questions
    from the study notes below.
    
    Rules:
    - Each question should have 4 options
    - Mention the correct answer
    - Keep questions concise
    - Focus on important concepts
    
    Notes:
    {text[:4000]}
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]