from src.fetch_data import fetch_drug_labels

def answer_question(question, medicine_name=None):
    records = fetch_drug_labels(limit=10)

    if not records:
        return "No drug information available."

    selected_drug = None

    if medicine_name:
        for drug in records:
            openfda = drug.get("openfda", {})
            brand_names = openfda.get("brand_name", [])
            generic_names = openfda.get("generic_name", [])

            all_names = [name.lower() for name in brand_names + generic_names]

            if medicine_name.lower() in all_names:
                selected_drug = drug
                break

    if not selected_drug:
        selected_drug = records[0]  # fallback

    purpose = selected_drug.get(
        "indications_and_usage",
        ["Information not available"]
    )[0]

    warnings = selected_drug.get(
        "warnings",
        ["No warnings available"]
    )[0]

    response = f"""
Drug Information Summary:

Medicine: {medicine_name if medicine_name else 'Sample Drug'}

Purpose:
{purpose}

Warnings:
{warnings}
"""
    return response
