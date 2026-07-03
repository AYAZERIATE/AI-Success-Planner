from ollama import chat


MODEL_NAME = "llama3.2"


def ask_ai(prompt):
    """
    Send a prompt to the Ollama model and return the response.
    """

    try:
        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content

    except Exception as e:
        return f"Error: {e}"