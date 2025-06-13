# Numerology calculation module
# utils/numerology.py

# utils/numerology.py

def get_life_path_info(name, dob):
    """
    Enhanced numerology details based on Life Path Number.
    """
    digits = [int(ch) for ch in dob if ch.isdigit()]
    life_path = reduce_to_single(sum(digits))

    return {
        "Life Path Number": life_path,
        "Personality Traits": get_life_path_traits(life_path),
        "Career Path": get_career_advice(life_path),
        "Love & Relationship": get_love_advice(life_path),
        "Health Guidance": get_health_advice(life_path),
        "Expression Number": 9,
        "Soul Urge Number": 9,
    }

def reduce_to_single(n):
    while n > 9 and n not in (11, 22):
        n = sum(int(d) for d in str(n))
    return n

def get_life_path_traits(num):
    return {
        1: "Leader, independent, innovative, driven by purpose.",
        2: "Diplomatic, sensitive, cooperative, peace-bringer.",
        3: "Creative, expressive, optimistic, loves communication.",
        4: "Practical, disciplined, stable, grounded worker.",
        5: "Adventurous, freedom-loving, curious, fast-changing.",
        6: "Nurturing, responsible, caretaker, community-oriented.",
        7: "Analytical, introspective, spiritual, truth-seeker.",
        8: "Ambitious, business-minded, power-driven, achiever.",
        9: "Humanitarian, compassionate, wise, emotionally evolved.",
        11: "Visionary, enlightened, highly intuitive, old soul.",
        22: "Master builder, legacy-creator, powerful manifestor."
    }.get(num, "Unique and evolving.")

def get_career_advice(num):
    return {
        1: "Start your own venture or lead a high-impact team.",
        2: "Excel in HR, diplomacy, healing or customer-facing roles.",
        3: "Thrive in media, writing, design, and creative fields.",
        4: "Ideal for engineering, logistics, real estate, admin roles.",
        5: "Dynamic jobs — marketing, travel, media, sales, PR.",
        6: "Healthcare, education, design, home business.",
        7: "Research, psychology, IT, spirituality, data science.",
        8: "Finance, management, law, politics — think CEO level.",
        9: "NGOs, teaching, healing, coaching, social leadership.",
        11: "Inspirational fields — counseling, film, spiritual coaching.",
        22: "Architecture, innovation, impact-driven leadership."
    }.get(num, "Explore broadly and follow your calling.")

def get_love_advice(num):
    return {
        1: "Needs independence in relationships, avoid dominance.",
        2: "Loyal and romantic, thrives with emotional bonding.",
        3: "Charming and flirtatious, needs fun and deep talk.",
        4: "Stable partner, seeks trust and lifelong commitment.",
        5: "Exciting partner but avoid routine; loves variety.",
        6: "Family-oriented, loving, sometimes overprotective.",
        7: "Emotionally guarded; needs time to open up deeply.",
        8: "High standards, loyal but sometimes controlling.",
        9: "Universal lover — empathetic, deeply emotional.",
        11: "Needs soul connection; romantic idealist.",
        22: "Deeply loyal but seeks someone who shares vision."
    }.get(num, "Love with honesty and self-awareness.")

def get_health_advice(num):
    return {
        1: "Watch blood pressure and stress-related issues.",
        2: "Avoid emotional eating; take care of digestion.",
        3: "Prone to throat, vocal cord, or sinus problems.",
        4: "Joint pain or bone stiffness over time — stretch!",
        5: "Restless energy — watch nerves, digestion, overwork.",
        6: "Hormonal balance and sugar levels need care.",
        7: "Mind-body imbalance — meditate and hydrate.",
        8: "Back pain and liver sensitivity — balance work-life.",
        9: "Over-giving leads to burnout; prioritize rest.",
        11: "Sensitive nervous system — avoid stimulants.",
        22: "Needs sleep, avoid overwork, prone to overload."
    }.get(num, "Live clean, stay active, sleep well.")

 
