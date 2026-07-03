from ai.ollama_client import ask_ai
def cv_generator():
    information = input("CV Creator (Press Enter to create your CV): ")

    if information == "":
              full_name = input("Enter your full name: ")
              phone_number = input("Enter your phone number: ")
              profile_text = input("Enter your profile summary: ")
              experience = input("Enter your experience: ")
              education = input("Enter your education: ")
              languages = input("Enter your languages: ")
              projects = input("Enter your projects: ")
              technical_skills = input("Enter your technical skills: ")

    prompt = f"""
                   Create a professional CV in Markdown format using the following information:

    Full Name: {full_name}
    Phone Number: {phone_number}
    Profile: {profile_text}
    Experience: {experience}
    Education: {education}
    Languages: {languages}
    Projects: {projects}
    Technical Skills: {technical_skills}

    Make the CV modern, professional, and well organized.
    """

    response = ask_ai(prompt)

    print("\n========== YOUR AI GENERATED CV ==========\n")
    print(response)
