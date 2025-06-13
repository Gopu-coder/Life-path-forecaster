import streamlit as st
from datetime import datetime
from utils import numerology, astrology, ml_model, tracker

st.set_page_config(page_title="🔮 Life Path Forecaster", layout="centered")

st.title("🧙‍♂️✨ Life Path Forecaster")
st.markdown("_Unlock your cosmic code with astrology, numerology, and a pinch of AI magic!_ 💫")

full_name = st.text_input("👤 Your Full Name")
dob = st.date_input("🎂 Date of Birth", value=datetime(1994, 2, 6))
birth_time = st.text_input("⏰ Time of Birth (HH:MM)", value="06:50")
birth_place = st.text_input("📍 Place of Birth", value="Dhenkanal, Odisha")

if st.button("🔍 Reveal My Future"):
    if not full_name or not dob:
        st.error("🚫 Please enter all required fields to reveal your destiny.")
    else:
        with st.spinner("🌌 Reading stars, decoding digits, consulting the AI gods..."):
            numerology_result = numerology.get_life_path_info(full_name, str(dob))
            astro_result = astrology.get_astrological_info(str(dob), birth_time, birth_place)
            life_predictions = ml_model.predict_major_life_events(str(dob), full_name)
            tracker.log_user_data(full_name, str(dob), {
                "numerology": numerology_result,
                "astrology": astro_result,
                "ml_predictions": life_predictions
            })

        # 🌟 Display Numerology
        st.header("🔢 Numerology Reading")
        st.markdown(f"**🔑 Life Path Number:** `{numerology_result['Life Path Number']}`")
        st.markdown(f"**🧠 Expression Number:** `{numerology_result['Expression Number']}`")
        st.markdown(f"**💓 Soul Urge Number:** `{numerology_result['Soul Urge Number']}`")
        st.markdown(f"**🧬 Personality Traits:** _{numerology_result['Personality Traits']}_")
        st.markdown(f"**📈 Career Path:** _{numerology_result['Career Path']}_")
        st.markdown(f"**❤️ Love Insight:** _{numerology_result['Love & Relationship']}_")
        st.markdown(f"**🩺 Health Guide:** _{numerology_result['Health Guidance']}_")
        st.markdown("🔮 _Psst... This number has guided mystics and millionaires alike._")

        # 🌠 Display Astrology
        st.header("🌠 Astrology Insight")
        st.markdown(f"**🌙 Moon Sign:** `{astro_result['Moon Sign']}`")
        st.markdown(f"**🌞 Rising Sign:** `{astro_result['Rising Sign']}`")
        st.markdown(f"**🪐 Moon Traits:** _{astro_result['Moon Traits']}_")
        st.markdown(f"**🧭 Rising Traits:** _{astro_result['Rising Traits']}_")
        st.markdown(f"**💘 Love Style:** _{astro_result['Love Style']}_")
        st.markdown(f"**📊 Career Drive:** _{astro_result['Career Drive']}_")
        st.markdown(f"**💉 Health Alert:** _{astro_result['Health Alert']}_")
        st.markdown("🪄 _You shine brightest under cosmic pressure!_")

        # 🤖 ML-Based Future Predictions
        st.header("📊 AI Future Forecast")

        st.subheader("🚀 Career Peaks")
        for event in life_predictions["Career Peaks"]:
            st.markdown(f"📅 **{event['year']}**: _{event['event']}_")

        st.subheader("💞 Relationship Timeline")
        for event in life_predictions["Relationship Timeline"]:
            st.markdown(f"📅 **{event['year']}**: _{event['event']}_")

        st.subheader("💰 Wealth Milestones")
        for event in life_predictions["Wealth Milestones"]:
            st.markdown(f"📅 **{event['year']}**: _{event['event']}_")

        st.success("✅ Your cosmic blueprint has been generated!")
        st.balloons()
        st.markdown("🧘‍♀️ _Don't take it too seriously... or do. The stars won't tell._ 🌟")
