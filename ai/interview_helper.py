from ai.ollama_client import ask_ai

answer = ask_ai("""
Create a list of the most popular interview questions for software developers.
For each question, provide a sample answer.
""")

print(answer)