from ai.ollama_client import ask_ai

def letter_generator():
    print("=== Professional Letter Generator ===")

    letter_type = input("Letter type: ")
    full_name = input("Your full name: ")
    company = input("Company name: ")
    position = input("Job position: ")

    prompt = f"""
    Write a professional {letter_type}.

    Name: {full_name}
    Company: {company}
    Position: {position}

    Make the letter formal and well organized.
    """

    answer = ask_ai(prompt)

    print("\n========== YOUR LETTER ==========\n")
    print(answer)