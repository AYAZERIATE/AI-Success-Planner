from ai.ollama_client import ask_ai

def generate_roadmap(career, duration):
    prompt = f"""
    Create a {duration}-month roadmap to become a {career}.

    Include:
    - Monthly learning plan
    - Skills to learn
    - Projects to build
    - Free resources
    - Tips for getting a job
    """

    return ask_ai(prompt)