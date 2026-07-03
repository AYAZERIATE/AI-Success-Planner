from ai.ollama_client import ask_ai

def map_helper():
    country = input("Enter your country: ")
    job = input("Enter your job: ")

    prompt = f"""
    I live in {country}.

    I am looking for a job as a {job}.

    List the best cities in {country} where I can find this job.

    For each city include:
    - City name
    - Why this city is a good choice
    - Industries or companies that usually hire for this job

    Return the answer in a clear list.
    """

    answer = ask_ai(prompt)

    print("\n========== JOB LOCATIONS ==========\n")
    print(answer)