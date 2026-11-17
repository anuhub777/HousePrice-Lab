
import streamlit as st
import pandas as pd
import textwrap
import joblib
import streamlit.components.v1 as components
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="HousePrice Lab",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    model = joblib.load(BASE_DIR / "models" / "house_price_model.pkl")
    defaults = joblib.load(BASE_DIR / "models" / "input_defaults.pkl")
    return model, defaults


model, defaults = load_model()

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
    --cream: #F5F2EB;
    --paper: #FFFEFA;
    --green: #263F35;
    --green-light: #E4EBE3;
    --muted: #85877E;
    --terracotta: #B96F50;
    --line: #E6E1D7;
}

.stApp {
    background: var(--cream);
    color: var(--green);
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Typography */

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--green) !important;
}

p, label, span {
    font-family: 'DM Sans', sans-serif;
}

/* Header */

.brand {
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 3px;
    color: var(--green);
}

.header-tag {
    color: var(--muted);
    font-size: 12px;
    letter-spacing: 1px;
    text-align: right;
}

/* Hero */

.hero {
    background: var(--green);
    border-radius: 20px;
    padding: 42px 45px;
    color: #F8F5ED;
    position: relative;
    overflow: hidden;
    min-height: 300px;
    margin-top: 25px;
    animation: fadeUp 0.7s ease both;
}

.hero h1 {
    color: #F8F5ED !important;
    font-size: 43px !important;
    line-height: 1.15;
    margin-bottom: 12px;
}

.hero p {
    color: #D0D9D0;
    font-size: 14px;
    max-width: 430px;
    line-height: 1.8;
}

.hero-kicker {
    color: #D6A58C;
    font-size: 10px;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 15px;
}

.hero-art {
    position: absolute;
    right: 3%;
    bottom: -12px;
    width: 42%;
    max-width: 420px;
    opacity: 0.95;
    animation: floatHouse 5s ease-in-out infinite;
}

/* Section headings */

.section-label {
    color: var(--terracotta);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    margin-bottom: 8px;
}

.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 27px;
    color: var(--green);
    margin-bottom: 5px;
}

.section-sub {
    color: var(--muted);
    font-size: 12px;
    margin-bottom: 22px;
}

/* Cards */

.stat-card {
    background: var(--green-light);
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 10px;
}

.stat-title {
    color: #6E7B6E;
    font-size: 10px;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

.stat-value {
    color: var(--green);
    font-size: 23px;
    font-weight: 700;
    margin-top: 5px;
}

.stat-caption {
    color: #7C897C;
    font-size: 10px;
}

/* Inputs */

div[data-testid="stNumberInput"],
div[data-testid="stSlider"] {
    margin-bottom: 13px;
}

label[data-testid="stWidgetLabel"] p {
    font-size: 12px !important;
    font-weight: 600 !important;
    color: #526257 !important;
}

div[data-baseweb="input"] {
    background: #FAF9F5;
    border-radius: 8px;
}

div[data-baseweb="input"] input {
    color: var(--green) !important;
}

div[data-testid="stNumberInput"] button {
    color: var(--green);
    border-color: var(--line);
}

/* Buttons */

.stButton > button {
    background: var(--green);
    color: #F8F5ED;
    border: none;
    border-radius: 9px;
    padding: 13px 22px;
    font-weight: 600;
    transition: all 0.25s ease;
    width: 100%;
}

.stButton > button:hover {
    background: #385747;
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 6px 18px #263F3525;
}

/* Prediction */

.prediction {
    background: #263F35;
    color: #F8F5ED;
    border-radius: 17px;
    padding: 27px;
    animation: fadeUp 0.6s ease both;
}

.prediction-label {
    color: #D6A58C;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
}

.prediction-value {
    font-family: 'Playfair Display', serif;
    color: #FFF9EC;
    font-size: 39px;
    margin: 10px 0;
}

.prediction-note {
    color: #CFD9D0;
    font-size: 11px;
}

/* Animations */

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes floatHouse {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-8px);
    }
}

@media (max-width: 768px) {
    .hero {
        padding: 28px;
        min-height: 420px;
    }

    .hero h1 {
        font-size: 34px !important;
    }

    .hero-art {
        width: 85%;
        right: 5%;
    }
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TOP NAVIGATION
# --------------------------------------------------

nav1, nav2 = st.columns([3, 1])

with nav1:
    st.markdown(
        '<div class="brand">⌂ HOUSEPRICE LAB</div>',
        unsafe_allow_html=True
    )

with nav2:
    st.markdown(
        '<div class="header-tag">REAL ESTATE · INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

hero_html = """
<!DOCTYPE html>
<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: 'DM Sans', sans-serif;
}

.hero {
    background: #263F35;
    border-radius: 20px;
    padding: 42px 45px;
    min-height: 300px;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    animation: fadeUp 0.7s ease both;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 480px;
}

.kicker {
    color: #D6A58C;
    font-size: 10px;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 15px;
}

h1 {
    font-family: 'Playfair Display', serif;
    color: #F8F5ED;
    font-size: 43px;
    line-height: 1.15;
    font-weight: 600;
    margin: 0 0 15px;
}

p {
    color: #D0D9D0;
    font-size: 14px;
    line-height: 1.8;
    max-width: 430px;
    margin: 0;
}

.house {
    position: absolute;
    width: 43%;
    max-width: 420px;
    right: 2%;
    bottom: -12px;
    animation: floatHouse 5s ease-in-out infinite;
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes floatHouse {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}

@media(max-width: 700px) {
    .hero {
        padding: 30px 25px;
        min-height: 440px;
        align-items: flex-start;
    }

    h1 {
        font-size: 34px;
    }

    .house {
        width: 85%;
        right: 5%;
    }
}
</style>
</head>

<body>
<div class="hero">

    <div class="hero-content">
        <div class="kicker">A SMARTER WAY TO VALUE PROPERTY</div>

        <h1>Every home has<br>a story. Find its value.</h1>

        <p>
            Explore the relationship between property characteristics
            and market value. Adjust the details of a home and discover
            what our machine learning model estimates it could be worth.
        </p>
    </div>

    <svg class="house" viewBox="0 0 440 280"
         xmlns="http://www.w3.org/2000/svg">

        <g opacity=".22" fill="none" stroke="#E6D9C7">
            <path d="M20 240 L420 240 M20 260 L420 260"/>
            <path d="M50 0 V280 M100 0 V280 M150 0 V280
                     M200 0 V280 M250 0 V280 M300 0 V280
                     M350 0 V280 M400 0 V280"/>
        </g>

        <path d="M70 145 L220 28 L370 145 V258 H70 Z"
              fill="#D8B99B"/>

        <path d="M45 151 L220 15 L395 151"
              fill="none" stroke="#F4E7D5" stroke-width="12"
              stroke-linecap="round" stroke-linejoin="round"/>

        <path d="M95 145 H345 V258 H95 Z" fill="#F0E7D6"/>

        <path d="M192 170 H248 V258 H192 Z" fill="#8D6650"/>

        <circle cx="238" cy="213" r="3" fill="#E8C69C"/>

        <rect x="117" y="169" width="51" height="49"
              rx="3" fill="#A8C2B2"/>

        <rect x="276" y="169" width="51" height="49"
              rx="3" fill="#A8C2B2"/>

        <path d="M142 169 V218 M117 193 H168
                 M301 169 V218 M276 193 H327"
              stroke="#F8F4E9" stroke-width="4"/>

        <path d="M82 258 H358" stroke="#E8D9C7" stroke-width="5"/>

        <path d="M30 258 Q50 235 75 258 M360 258 Q385 235 410 258"
              fill="none" stroke="#B9C9A9" stroke-width="10"/>

        <circle cx="80" cy="205" r="19" fill="#829B7C"/>
        <circle cx="80" cy="180" r="14" fill="#9CAF8C"/>

        <circle cx="365" cy="205" r="19" fill="#829B7C"/>
        <circle cx="365" cy="180" r="14" fill="#9CAF8C"/>

    </svg>
</div>
</body>
</html>
"""

components.html(
    hero_html,
    height=320,
    scrolling=False
)


# --------------------------------------------------
# PROPERTY CONFIGURATION
# --------------------------------------------------

st.markdown(
    '<div class="section-label">01 — PROPERTY CONFIGURATION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-heading">Design your property profile</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-sub">'
    'Adjust the property details below to explore its estimated market value.'
    '</div>',
    unsafe_allow_html=True
)

left, right = st.columns([1.5, 1], gap="large")

# --------------------------------------------------
# PROPERTY INPUTS
# --------------------------------------------------

with left:

    with st.container(border=True):

        st.markdown("### The property")

        st.caption(
            "Tell us about the home's size, layout and construction."
        )

        col1, col2 = st.columns(2)

        with col1:

            overall_qual = st.slider(
                "Overall Quality",
                min_value=1,
                max_value=10,
                value=5,
                help="Overall material and finish quality."
            )

            gr_liv_area = st.number_input(
                "Living Area (sq. ft.)",
                min_value=100,
                max_value=10000,
                value=1500,
                step=50
            )

            garage_cars = st.number_input(
                "Garage Capacity",
                min_value=0,
                max_value=5,
                value=2
            )

            total_bsmt_sf = st.number_input(
                "Basement Area (sq. ft.)",
                min_value=0,
                max_value=5000,
                value=800,
                step=50
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
                value=1000,
                step=50
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
                value=8000,
                step=100
            )

            year_remod = st.number_input(
                "Year Remodeled",
                min_value=1800,
                max_value=2026,
                value=2005
            )

            bedrooms = st.number_input(
                "Bedrooms",
                min_value=0,
                max_value=10,
                value=3
            )

# --------------------------------------------------
# LIVE PROPERTY OVERVIEW
# --------------------------------------------------

with right:

    st.markdown(
        '<div class="section-label">YOUR PROPERTY</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-heading">A closer look</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-sub">'
        'A live overview of your selected property.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-title">Living space</div>
        <div class="stat-value">
            {gr_liv_area:,}
            <span style="font-size:12px">sq. ft.</span>
        </div>
        <div class="stat-caption">Above-ground living area</div>
    </div>

    <div class="stat-card">
        <div class="stat-title">Property quality</div>
        <div class="stat-value">
            {overall_qual}
            <span style="font-size:13px">/ 10</span>
        </div>
        <div class="stat-caption">Overall construction and finish</div>
    </div>

    <div class="stat-card">
        <div class="stat-title">Built in</div>
        <div class="stat-value">{year_built}</div>
        <div class="stat-caption">
            Age: {2026 - year_built} years
        </div>
    </div>

    <div class="stat-card">
        <div class="stat-title">Bedrooms & bathrooms</div>
        <div class="stat-value">
            {bedrooms}
            <span style="font-size:13px">bedrooms</span>
            <span style="font-size:13px"> · {full_bath} baths</span>
        </div>
        <div class="stat-caption">Above-ground bedrooms</div>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# PREDICTION SECTION
# --------------------------------------------------

st.write("")

st.markdown(
    '<div class="section-label">02 — PROPERTY VALUATION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-heading">'
    'Discover your home\'s estimated value'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-sub">'
    'Ready to see what your property could be worth?'
    '</div>',
    unsafe_allow_html=True
)

if st.button("Estimate Property Value  →", type="primary"):

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

    st.write("")

    prediction_html = textwrap.dedent(f"""
    <div class="prediction">
        <div class="prediction-label">
            YOUR ESTIMATED PROPERTY VALUE
        </div>
        <div class="prediction-value">
            ${prediction:,.2f}
        </div>
        <div class="prediction-note">
            Generated using our trained Random Forest regression model.
            This is a model estimate, not a professional property appraisal.
        </div>
    </div>
    """)

    st.markdown(prediction_html, unsafe_allow_html=True)

    st.balloons()

    st.write("")

    st.caption(
        "HousePrice Lab · Machine Learning powered property valuation"
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

footer1, footer2 = st.columns([3, 1])

with footer1:
    st.caption(
        "HOUSEPRICE LAB · EXPLORING THE SCIENCE OF PROPERTY VALUATION"
    )

with footer2:
    st.caption("BUILT WITH STREAMLIT")
