import streamlit as st
from datetime import datetime
from utils import numerology, astrology, ml_model

st.set_page_config(page_title="🔮 Life Path Forecaster", layout="centered")

st.title("🔮 Life Path Forecaster")
st.markdown("_✨ Discover what the stars, numbers, and some ancient cosmic tea say about your life!_")

full_name = st.text_input("🧑 Full Name")
dob = st.date_input("📅 Date of Birth", value=datetime(1994, 2, 6))
birth_time = st.text_input("⏰ Time of Birth (HH:MM)", value="06:50")
birth_place = st.text_input("🌍 Place of Birth", value="Dhenkanal, Odisha")

if st.button("🔍 Reveal My Cosmic Destiny"):
    if not full_name or not dob:
        st.error("🚫 Please enter all required fields to unlock your fate.")
    else:
        with st.spinner("🪄 Consulting the cosmos, decoding numbers..."):
            numerology_result = numerology.get_life_path_info(full_name, str(dob))
            astro_result = astrology.get_astrological_info(str(dob), birth_time, birth_place)
            life_predictions = ml_model.predict_major_life_events(str(dob), full_name)

        st.header("🔢 Numerology Reading")
        st.markdown(f"**🔑 Life Path Number:** {numerology_result['Life Path Number']}")
        st.markdown(f"**😎 Personality Traits:** {numerology_result['Personality Traits']}")
        st.markdown(f"**💼 Career Vibes:** {numerology_result['Career Path']}")
        st.markdown(f"**💖 Love Forecast:** {numerology_result['Love & Relationship']}")
        st.markdown(f"**🩺 Health Notes:** {numerology_result['Health Guidance']}")
        st.markdown(f"**🧠 Expression Number:** {numerology_result['Expression Number']}")
        st.markdown(f"**🔥 Soul Urge Number:** {numerology_result['Soul Urge Number']}")
        st.markdown("🧙 _Rumor says someone with your Life Path Number once became a time traveler in 1892... coincidence?_")

        st.header("🌠 Astrology Vibes")
        st.markdown(f"**🌙 Moon Sign:** {astro_result['Moon Sign']}")
        st.markdown(f"**🧵 Moon Traits:** {astro_result['Moon Traits']}")
        st.markdown(f"**🌅 Rising Sign:** {astro_result['Rising Sign']}")
        st.markdown(f"**✨ Rising Traits:** {astro_result['Rising Traits']}")
        st.markdown(f"**💘 Love Style:** {astro_result['Love Style']}")
        st.markdown(f"**📈 Career Drive:** {astro_result['Career Drive']}")
        st.markdown(f"**🚨 Health Alert:** {astro_result['Health Alert']}")
        st.markdown("🔭 _Astrologers agree: people with your Moon-Rising combo tend to find snacks in mysterious places._")

        st.header("📊 Life Timeline Predictions")

        st.subheader("🚀 Career Peaks")
        for event in life_predictions["Career Peaks"]:
            st.markdown(f"- **{event['year']}**: {event['event']}")

        st.subheader("💞 Relationship Timeline")
        for event in life_predictions["Relationship Timeline"]:
            st.markdown(f"- **{event['year']}**: {event['event']}")

        st.subheader("💰 Wealth Milestones")
        for event in life_predictions["Wealth Milestones"]:
            st.markdown(f"- **{event['year']}**: {event['event']}")

        st.markdown("_🤖 These are AI-generated forecasts — believe them only if you're into time travel!_")
        st.success("🔓 Your cosmic forecast has been unlocked!")
