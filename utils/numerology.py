# utils/numerology.py

def get_life_path_info(name, dob):
    from datetime import datetime

    def calculate_life_path(dob):
        digits = [int(char) for char in dob if char.isdigit()]
        while len(digits) > 1:
            digits = [int(x) for x in str(sum(digits))]
        return digits[0]

    def reduce_number(n):
        while n > 9 and n not in (11, 22, 33):
            n = sum(int(d) for d in str(n))
        return n

    full_name = name.replace(" ", "").upper()
    vowels = 'AEIOU'

    expression_number = reduce_number(sum(ord(c) - 64 for c in full_name if c.isalpha()))
    soul_urge_number = reduce_number(sum(ord(c) - 64 for c in full_name if c in vowels))

    lp_number = calculate_life_path(dob)

    traits = {
        1: "Leader, independent, ambitious",
        2: "Diplomatic, sensitive, supportive",
        3: "Creative, social, optimistic",
        4: "Hardworking, practical, reliable",
        5: "Adventurous, dynamic, curious",
        6: "Responsible, nurturing, harmonious",
        7: "Analytical, spiritual, introspective",
        8: "Powerful, goal-oriented, disciplined",
        9: "Compassionate, wise, humanitarian",
    }

    career = {
        1: "Entrepreneur, CEO, Inventor",
        2: "Counselor, Diplomat, Advisor",
        3: "Artist, Performer, Public Speaker",
        4: "Engineer, Analyst, Administrator",
        5: "Marketing, Sales, Explorer",
        6: "Teacher, Healer, Caregiver",
        7: "Scientist, Philosopher, Mystic",
        8: "Executive, Lawyer, Financier",
        9: "Social Worker, Philanthropist, Writer",
    }

    love = {
        1: "Needs respect and admiration",
        2: "Seeks emotional connection",
        3: "Flirty and expressive",
        4: "Loyal and security-driven",
        5: "Passionate and spontaneous",
        6: "Devoted and romantic",
        7: "Private and selective",
        8: "Strong-willed but caring",
        9: "Loving and idealistic",
    }

    health = {
        1: "Watch for head-related issues",
        2: "Sensitive digestion or stress",
        3: "Throat or vocal strain",
        4: "Back pain or rigidity",
        5: "Nervous energy, sleep issues",
        6: "Heart health, emotional strain",
        7: "Immune sensitivity",
        8: "Joint or bone stress",
        9: "Circulation and blood pressure",
    }

    return {
        "Life Path Number": lp_number,
        "Expression Number": expression_number,
        "Soul Urge Number": soul_urge_number,
        "Personality Traits": traits.get(lp_number, "Unique and mysterious"),
        "Career Path": career.get(lp_number, "Uncharted brilliance"),
        "Love & Relationship": love.get(lp_number, "Love in your own language"),
        "Health Guidance": health.get(lp_number, "Stay mindful and balanced")
    }


# utils/astrology.py

def get_astrological_info(dob, birth_time, birth_place):
    # This is a mock version. In a real-world app, you'd use an astrology API or ephemeris

    import random
    moon_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    rising_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    moon = random.choice(moon_signs)
    rising = random.choice(rising_signs)

    moon_traits = {
        "Cancer": "Deeply intuitive and nurturing",
        "Pisces": "Imaginative and emotional",
        "Aries": "Fiery emotions, quick reactions",
        "Leo": "Dramatic and passionate",
        "Virgo": "Emotionally reserved but loyal",
        "Scorpio": "Intense and deeply emotional",
        "Gemini": "Emotionally curious and witty",
        "Libra": "Emotionally fair and romantic",
        "Taurus": "Steady and emotionally secure",
        "Capricorn": "Disciplined and serious",
        "Sagittarius": "Optimistic and fun-loving",
        "Aquarius": "Detached but humanitarian",
    }

    rising_traits = {
        "Virgo": "Organized, perfectionist, analytical",
        "Capricorn": "Ambitious, grounded, patient",
        "Gemini": "Witty, quick-thinker, adaptable",
        "Leo": "Charismatic, warm, proud",
        "Scorpio": "Intense, magnetic, mysterious",
        "Cancer": "Protective, home-loving, sensitive",
        "Aries": "Bold, assertive, pioneering",
        "Taurus": "Stable, sensual, methodical",
        "Libra": "Charming, stylish, diplomatic",
        "Sagittarius": "Adventurous, blunt, wise",
        "Pisces": "Dreamy, spiritual, gentle",
        "Aquarius": "Innovative, quirky, unique",
    }

    love_style = {
        "Leo": "Loyal but loves to be adored",
        "Cancer": "Nurturing and deeply emotional",
        "Scorpio": "Passionate and intense",
        "Libra": "Romantic and aesthetically driven",
        "Virgo": "Practical but caring",
        "Pisces": "Loving and dreamy",
        "Taurus": "Grounded, sensual and committed",
        "Gemini": "Flirtatious and talkative",
        "Aries": "Bold and straightforward",
        "Capricorn": "Steady and responsible",
        "Aquarius": "Independent and unconventional",
        "Sagittarius": "Free-spirited and fun",
    }

    career_drive = {
        "Leo": "Desires recognition and creativity",
        "Capricorn": "Seeks authority and results",
        "Virgo": "Driven by mastery and logic",
        "Scorpio": "Wants control and transformation",
        "Gemini": "Thrives on learning and sharing",
        "Aries": "Boldly chases leadership roles",
        "Pisces": "Wants to heal and inspire",
        "Aquarius": "Innovates for the collective",
    }

    health_alert = {
        "Leo": "Heart health focus",
        "Virgo": "Digestive sensitivity",
        "Scorpio": "Reproductive and hormonal",
        "Pisces": "Immune and lymphatic watch",
        "Capricorn": "Bones and joints care",
        "Cancer": "Stomach and breast concerns",
        "Aries": "Headaches and migraines",
        "Gemini": "Lungs and nerves awareness",
    }

    return {
        "Moon Sign": moon,
        "Rising Sign": rising,
        "Moon Traits": moon_traits.get(moon, "Emotionally expressive and changeable"),
        "Rising Traits": rising_traits.get(rising, "Complex and evolving persona"),
        "Love Style": love_style.get(moon, "Loves in mysterious ways"),
        "Career Drive": career_drive.get(rising, "Career through unique talent"),
        "Health Alert": health_alert.get(moon, "General balance is key")
    }
