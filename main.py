from src.rag_pipeline import answer_question
from src.reminder import generate_reminder

if __name__ == "__main__":
    print("Welcome to MediMind")

    medicine = input("Enter medicine name: ")
    question = input("Ask your question: ")

    response = answer_question(question, medicine)
    reminder = generate_reminder(medicine)

    print("\n--- AI Response ---")
    print(response)

    print("\n--- Medication Reminder ---")
    print(reminder)
