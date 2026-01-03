from fetch_data import fetch_drug_labels

def answer_question(question):
    records = fetch_drug_labels()

    if not records:
        return "No drug information available."

    drug = records[0]

    purpose = drug.get("indications_and_usage", ["Information not available"])[0]
    warnings = drug.get("warnings", ["No warnings available"])[0]

    response = f"""
Drug Information Summary:

Purpose:
{purpose}

Warnings:
{warnings}
"""
    return response
