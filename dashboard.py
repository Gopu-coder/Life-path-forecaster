# Streamlit dashboard code will go here
import streamlit as st
from utils import numerology, astrology, ml_model  # Make sure these files exist

st.set_page_config(page_title="🔮 Life Path Forecaster", layout="centered")

st.title("🔮 Life Path Forecaster")

# Input Section
st.header("Enter Your Details")

full_name = st.text_input("Full Name")
import datetime
dob = st.date_input(
    "Date of Birth",
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date.today(),
    value=datetime.date(1990, 1, 1)
)

birth_time = st.time_input("Time of Birth")
birth_place = st.text_input("Place of Birth (City, Country)")

# Predict Button
if st.button("🔍 Predict My Future"):

    if not full_name or not birth_place:
        st.warning("Please fill in all fields.")
    else:
        # Basic Numerology Prediction
        numerology_result = numerology.get_life_path_info(full_name, str(dob))
        st.subheader("🧮 Numerology Reading")
        st.write(f"**Life Path Number:** {numerology_result.get('life_path_number', '-')}")
        st.write(f"**Expression Number:** {numerology_result.get('expression_number', '-')}")
        st.write(f"**Soul Urge Number:** {numerology_result.get('soul_urge_number', '-')}")

        # Astrology Prediction (if available)
        try:
            astro = astrology.get_basic_astrology(str(dob), str(birth_time), birth_place)
            st.subheader("🌌 Astrology Insight")
            st.write(f"**Moon Sign:** {astro.get('moon_sign', '-')}")
            st.write(f"**Rising Sign:** {astro.get('ascendant', '-')}")
        except Exception as e:
            st.warning("Astrology prediction could not be completed. Please check birth info.")
# --- ML MODEL PREDICTION ---
  ml_prediction = ml_model.predict_future(
    full_name,
    str(dob),
    numerology_result.get("life_path_number", 0),
    astro.get("moon_sign", ""),
    astro.get("ascendant", "")
)

st.subheader("🤖 Life Prediction Engine (AI-Based)")
st.write(f"**Age:** {ml_prediction['age']}")
st.write(f"**Phase of Life:** {ml_prediction['predicted_phase']}")
st.write("**Predicted Traits:**")
for trait in ml_prediction["highlighted_traits"]:
    st.markdown(f"- {trait}")

        st.success("✅ Prediction complete!")

