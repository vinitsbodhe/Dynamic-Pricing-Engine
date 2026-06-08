import streamlit as st
import joblib

from src.pricing_engine import predict_and_recommend


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Dynamic Pricing Engine",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 Hotel Dynamic Pricing Engine")


# -----------------------------
# LOAD MODEL
# -----------------------------

rf = joblib.load("models/hotel_pricing_model.pkl")

training_columns = joblib.load(
    "models/training_columns.pkl"
)


# -----------------------------
# INPUTS
# -----------------------------

st.subheader("Booking Details")

col1, col2 = st.columns(2)

with col1:

    hotel = st.selectbox(
        "Hotel Type",
        ["City Hotel", "Resort Hotel"]
    )

    month = st.selectbox(
        "Arrival Month",
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
    )

    market_segment = st.selectbox(
        "Market Segment",
        [
            "Online TA",
            "Offline TA/TO",
            "Direct",
            "Groups",
            "Corporate",
            "Aviation",
            "Complementary"
        ]
    )

with col2:

    lead_time = st.number_input(
        "Lead Time",
        min_value=0,
        value=30
    )

    adults = st.number_input(
        "Adults",
        min_value=1,
        value=2
    )

    children = st.number_input(
        "Children",
        min_value=0,
        value=0
    )

    babies = st.number_input(
        "Babies",
        min_value=0,
        value=0
    )


# -----------------------------
# PREDICT BUTTON
# -----------------------------

if st.button("Generate Recommendation"):

    booking = {

        "hotel": hotel,

        "lead_time": lead_time,

        "arrival_date_month": month,

        "market_segment": market_segment,

        # default values

        "distribution_channel": "TA/TO",

        "customer_type": "Transient",

        "adults": adults,

        "children": children,

        "babies": babies,

        "previous_cancellations": 0,

        "booking_changes": 0
    }

    result = predict_and_recommend(
        booking,
        rf,
        training_columns
    )

    st.divider()

    st.subheader("Pricing Recommendation")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Predicted ADR",
            f"{result['Predicted ADR']:.2f}"
        )

    with c2:
        st.metric(
            "Demand Score",
            f"{result['Demand Score']:.0f}"
        )

    with c3:
        st.metric(
            "Risk Score",
            f"{result['Risk Score']:.0f}"
        )

    c4, c5 = st.columns(2)

    with c4:
        st.metric(
            "Adjustment %",
            f"{result['Adjustment %']:.2f}%"
        )

    with c5:
        st.metric(
            "Recommended ADR",
            f"{result['Recommended ADR']:.2f}"
        )


