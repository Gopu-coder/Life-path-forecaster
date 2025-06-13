# Astrology calculation module
# utils/astrology.py

def get_basic_astrology(dob_str, tob_str, pob_str):
    """
    Simple mock astrology logic. Returns basic predictions for now.
    Replace this with real astrological calculations later.
    """
    from datetime import datetime

    # Convert input to usable format
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    hour = int(tob_str.split(":")[0])
    
    # Basic moon sign mock (based on birth month)
    moon_signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    moon_sign = moon_signs[dob.month % 12]

    # Basic ascendant (rising sign) mock (based on hour)
    ascendants = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    ascendant = ascendants[hour % 12]

    return {
        "moon_sign": moon_sign,
        "ascendant": ascendant
    }
