# utils/astrology.py

def get_astrological_info(dob, birth_time, birth_place):
    # Mock moon and rising sign based on birth time/place (static for now)
    moon_sign = "Leo"
    rising_sign = "Capricorn"

    moon_traits = {
        "Aries": "🔥 Bold, emotional surges, quick to love and fight.",
        "Taurus": "🌳 Steady and nurturing, craves comfort and stability.",
        "Gemini": "🌀 Emotionally witty and curious, loves variety.",
        "Cancer": "🌊 Deeply intuitive, sensitive, and caring.",
        "Leo": "🌟 Proud-hearted, dramatic, generous in love.",
        "Virgo": "📋 Anxious but thoughtful, shows love through action.",
        "Libra": "⚖️ Seeks emotional balance, diplomatic and charming.",
        "Scorpio": "🦂 Intense, transformative emotions, magnetic presence.",
        "Sagittarius": "🏹 Free-spirited, optimistic, emotional adventurer.",
        "Capricorn": "🪨 Reserved, emotionally strong, goal-driven.",
        "Aquarius": "🚀 Detached but idealistic, loves humanity.",
        "Pisces": "🎭 Dreamy, emotionally porous, artistic and soulful."
    }

    rising_traits = {
        "Aries": "⚔️ Bold, direct, and assertive energy.",
        "Taurus": "🌼 Calm presence, dependable and grounded.",
        "Gemini": "🗣️ Talkative and youthful energy.",
        "Cancer": "🍼 Nurturing aura and approachable.",
        "Leo": "🎬 Natural leader with flair and confidence.",
        "Virgo": "🧠 Observant, detail-oriented, and well-mannered.",
        "Libra": "💞 Graceful, charming, and balanced.",
        "Scorpio": "🕶️ Mysterious and intense outward vibe.",
        "Sagittarius": "🌍 Adventurous, inspiring and bold.",
        "Capricorn": "🏛️ Responsible and authoritative first impression.",
        "Aquarius": "👽 Quirky, unconventional and intelligent.",
        "Pisces": "🌙 Soft, dreamy, and empathetic."
    }

    love_styles = {
        "Leo": "🔥 Passionate, loyal, and loves grand gestures.",
        "Capricorn": "🪨 Committed, slow to warm up, but fiercely devoted."
    }

    career_drives = {
        "Leo": "🎤 Thrive in spotlight roles – leadership, media, creativity.",
        "Capricorn": "📈 Ambitious planners – thrive in corporate or structured paths."
    }

    health_tips = {
        "Leo": "💓 Take care of your heart and avoid overexertion.",
        "Capricorn": "🦴 Watch your bones, knees, and joints."
    }

    return {
        "Moon Sign": moon_sign,
        "Rising Sign": rising_sign,
        "Moon Traits": moon_traits[moon_sign],
        "Rising Traits": rising_traits[rising_sign],
        "Love Style": love_styles[moon_sign],
        "Career Drive": career_drives[rising_sign],
        "Health Alert": health_tips[rising_sign]
    }
