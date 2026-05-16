import ollama

def summarize_notes(text):

    prompt = f"""
        You are an AI Study Assistant.

        Summarize the study notes below for students.

        Rules:
        - Use simple language
        - Keep it concise
        - Use bullet points
        - Highlight key concepts
        - Mention important examples if needed
        - Make revision easy

        Notes:
{text[:4000]}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
