from src.rag_pipeline import answer_question

if __name__ == "__main__":
    print("Welcome to MediMind")

    medicine = input("Enter medicine name: ")
    question = input("Ask your question: ")

    response = answer_question(question, medicine)

    print("\n--- AI Response ---")
    print(response)
