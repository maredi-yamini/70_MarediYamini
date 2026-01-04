def generate_reminder(medicine_name):
    """
    Generate a simple medication reminder plan.
    """
    return {
        "medicine": medicine_name,
        "schedule": ["Morning", "Night"],
        "message": f"Please take {medicine_name} as prescribed."
    }
