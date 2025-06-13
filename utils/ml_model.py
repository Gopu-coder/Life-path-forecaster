# Machine learning trend predictor
# utils/ml_model.py

def predict_future(name, dob, life_path, moon_sign, ascendant):
    """
    Mock ML model logic. In a real case, you'd load a trained model here.
    """
    from datetime import datetime

    # Convert DOB to age
    birth_year = int(dob.split("-")[0])
    current_year = datetime.now().year
    age = current_year - birth_year

    # Create fake "predicted traits" based on inputs
    traits = []

    if life_path in [1, 8]:
        traits.append("Strong leadership qualities")
    if moon_sign in ["Cancer", "Pisces"]:
        traits.append("Emotionally intuitive and creative")
    if ascendant in ["Virgo", "Capricorn"]:
        traits.append("Practical and goal-oriented")
    if life_path == 7:
        traits.append("Spiritual growth ahead")

    # Add age-based phase
    if age < 25:
        phase = "Learning & exploration phase"
    elif age < 40:
        phase = "Career consolidation & financial opportunities"
    else:
        phase = "Wisdom, mentorship, and legacy building"

    return {
        "age": age,
        "predicted_phase": phase,
        "highlighted_traits": traits
    }
def predict_major_life_events(dob, name):
    return {
        "Career Peaks": [
            {"year": 2026, "event": "Promoted to Lead Role"},
            {"year": 2030, "event": "Started Own Business"},
            {"year": 2035, "event": "Became Industry Mentor"}
        ],
        "Relationship Timeline": [
            {"year": 2027, "event": "Met Life Partner"},
            {"year": 2029, "event": "Got Married"},
            {"year": 2032, "event": "Welcomed First Child"}
        ],
        "Wealth Milestones": [
            {"year": 2028, "event": "Bought First Home"},
            {"year": 2033, "event": "Reached Financial Independence"},
            {"year": 2040, "event": "Early Retirement Option"}
        ]
    }

