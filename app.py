from ai.cv_generator import cv_generator
from ai.interview_helper import interview_helper
from ai.job_makers import job_makers
from ai.letter_generator import letter_generator
from ai.map_helper import map_helper
from ai.roadmap_generator import generate_roadmap


def main():
    while True:
        print("\n" + "=" * 50)
        print("        AI SUCCESS PLANNER")
        print("=" * 50)

        print("1. AI CV generator")
        print("2. AI Interview Helper")
        print("3. AI Job Maker")
        print("4. AI Professional Letter Generator")
        print("5. AI Job Location Helper")
        print("6. AI Career Roadmap Generator")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            cv_genarator()

        elif choice == "2":
            interview_helper()

        elif choice == "3":
            job_makers()

        elif choice == "4":
            letter_generator()

        elif choice == "5":
            map_helper()

        elif choice == "6":
            career = input("Enter your dream career: ")
            duration = input("Enter roadmap duration (3, 6, or 12 months): ")

            roadmap = generate_roadmap(career, duration)

            print("\n========== YOUR CAREER ROADMAP ==========\n")
            print(roadmap)

        elif choice == "0":
            print("\nThank you for using AI Success Planner!")
            print("Good luck achieving your goals.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()