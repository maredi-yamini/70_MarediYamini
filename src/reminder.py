def generate_reminder(medicine_name, times_per_day):
    """
    Generate a simple medication reminder plan.
    """
    reminder = {
        "medicine": medicine_name,
        "times_per_day": times_per_day,
        "message": "Please take your medicine as prescribed."
    }
    return reminder
