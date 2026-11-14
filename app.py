import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="HousePrice Lab",
    page_icon="🏠",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"
model = joblib.load(MODEL_PATH)

DEFAULTS_PATH = BASE_DIR / "models" / "input_defaults.pkl"
defaults = joblib.load(DEFAULTS_PATH)

st.title("🏠 HousePrice Lab")
st.write("Predict house sale prices using Machine Learning.")

st.divider()

st.subheader("Enter House Details")

col1, col2 = st.columns(2)

with col1:
    overall_qual = st.slider(
        "Overall Quality",
        min_value=1,
        max_value=10,
        value=5
    )

    gr_liv_area = st.number_input(
        "Above Ground Living Area (sq. ft.)",
        min_value=100,
        max_value=10000,
        value=1500
    )

    garage_cars = st.number_input(
        "Garage Capacity",
        min_value=0,
        max_value=5,
        value=2
    )

    total_bsmt_sf = st.number_input(
        "Total Basement Area (sq. ft.)",
        min_value=0,
        max_value=5000,
        value=800
    )

    year_built = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2026,
        value=2000
    )

with col2:
    first_flr_sf = st.number_input(
        "First Floor Area (sq. ft.)",
        min_value=100,
        max_value=5000,
        value=1000
    )

    full_bath = st.number_input(
        "Full Bathrooms",
        min_value=0,
        max_value=5,
        value=2
    )

    lot_area = st.number_input(
        "Lot Area (sq. ft.)",
        min_value=500,
        max_value=100000,
        value=8000
    )

    year_remod = st.number_input(
        "Year Remodeled",
        min_value=1800,
        max_value=2026,
        value=2005
    )

    bedrooms = st.number_input(
        "Bedrooms Above Ground",
        min_value=0,
        max_value=10,
        value=3
    )

if st.button("Predict House Price", type="primary"):

    input_data = defaults.copy()

    input_data.update({
        "OverallQual": overall_qual,
        "GrLivArea": gr_liv_area,
        "GarageCars": garage_cars,
        "TotalBsmtSF": total_bsmt_sf,
        "YearBuilt": year_built,
        "1stFlrSF": first_flr_sf,
        "FullBath": full_bath,
        "LotArea": lot_area,
        "YearRemodAdd": year_remod,
        "BedroomAbvGr": bedrooms
    })

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    st.divider()
    st.subheader("Estimated House Price")

    st.success(f"${prediction:,.2f}")

    st.caption(
        "Prediction generated using our trained "
        "Random Forest regression model."
    )