# Astrology calculation module
# utils/astrology.py

# utils/astrology.py

def get_astrological_info(dob, birth_time, birth_place):
    """
    Rule-based astrology traits based on DOB and time.
    """
    if "02" in dob or "Feb" in dob:
        moon_sign = "Leo"
    else:
        moon_sign = "Aquarius"

    hour = int(birth_time.split(":")[0]) if birth_time else 6
    rising_sign = "Capricorn" if hour < 7 else "Gemini"

    return {
        "Moon Sign": moon_sign,
        "Moon Traits": get_moon_sign_traits(moon_sign),
        "Rising Sign": rising_sign,
        "Rising Traits": get_rising_sign_traits(rising_sign),
        "Love Style": get_love_style(moon_sign),
        "Career Drive": get_career_drive(moon_sign),
        "Health Alert": get_health_pattern(moon_sign),
    }

def get_moon_sign_traits(sign):
    return {
        "Leo": "Emotionally bold, needs love and appreciation.",
        "Aquarius": "Detached but idealistic, mentally sharp.",
        "Cancer": "Deeply caring, nostalgic, mood-sensitive.",
        "Virgo": "Practical but anxious, self-critical emotions.",
        "Scorpio": "Intense, mysterious, emotionally deep.",
        "Sagittarius": "Happy-go-lucky, open-hearted, freedom-loving."
    }.get(sign, "Emotionally unique and evolving.")

def get_rising_sign_traits(sign):
    return {
        "Capricorn": "Appears mature, responsible, ambitious.",
        "Gemini": "Talkative, witty, curious; always learning.",
        "Aries": "Direct, brave, fiery in first impressions.",
        "Pisces": "Soft-spoken, dreamy, imaginative aura.",
        "Libra": "Charming, fair, graceful public image."
    }.get(sign, "Unique presence and evolving nature.")

def get_love_style(sign):
    return {
        "Leo": "Loyal and generous lover, needs praise.",
        "Aquarius": "Detached but loyal once committed.",
        "Cancer": "Emotionally bonded, nurturing, clingy.",
        "Sagittarius": "Playful, adventurous, hates control.",
        "Scorpio": "Intense, passionate, jealous at times.",
        "Virgo": "Caring in actions, slow to express verbally."
    }.get(sign, "Express love your own way.")

def get_career_drive(sign):
    return {
        "Leo": "Craves recognition — great in media or leadership.",
        "Aquarius": "Tech-savvy, thrives in innovation.",
        "Cancer": "Best in healing, hospitality, nurturing fields.",
        "Sagittarius": "Travel, teaching, philosophy, public roles.",
        "Scorpio": "Detectives, analysts, surgeons, secrets.",
        "Virgo": "Healthcare, research, detailed service jobs."
    }.get(sign, "Explore and find what drives you.")

def get_health_pattern(sign):
    return {
        "Leo": "Heart and spine sensitivity. Do cardio, avoid ego stress.",
        "Aquarius": "Circulation and lower leg issues. Stretch often.",
        "Cancer": "Stomach and chest area prone. Eat light, avoid dairy excess.",
        "Scorpio": "Reproductive health and hormonal balance.",
        "Sagittarius": "Hips, thighs, liver. Avoid overindulgence.",
        "Virgo": "Gut health, intestines, worry-driven tension."
    }.get(sign, "Listen to your body daily.")
