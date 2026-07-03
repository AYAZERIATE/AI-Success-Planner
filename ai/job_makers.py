from ai.ollama_client import ask_ai

country = input("Enter your country: ")
field = input("Enter your field (IT, Healthcare, Marketing, etc.): ")

prompt = f"""
I live in {country}.
Generate the best job opportunities in the {field} field.

For each job include:
- Job title
- Required skills
- Experience level
- Career growth
"""

answer = ask_ai(prompt)

print(answer)