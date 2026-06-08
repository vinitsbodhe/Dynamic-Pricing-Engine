import pandas as pd


month_score = {
    'July': 1,
    'August': 1,
    'May': 1,

    'March': 0.5,
    'April': 0.5,
    'June': 0.5,
    'September': 0.5,
    'October': 0.5,

    'January': 0,
    'February': 0,
    'November': 0,
    'December': 0
}

hotel_score = {
    'City Hotel': 1,
    'Resort Hotel': 0.7
}

platform_score = {
    'Online TA': 1,
    'Direct': 0.8,
    'Aviation': 0.6,
    'Offline TA/TO': 0.4,
    'Groups': 0.2
}


def lead_time_score(lead_time):

    if lead_time > 180:
        return 1

    elif lead_time > 90:
        return 0.6

    elif lead_time > 30:
        return 0.3

    return 0


def calculate_demand_score(
    month,
    hotel,
    market_segment
):

    score = (
        0.6 * month_score.get(month, 0)
        + 0.2 * hotel_score.get(hotel, 0)
        + 0.2 * platform_score.get(market_segment, 0)
    )

    return score * 100


def calculate_risk_score(
    lead_time,
    market_segment
):

    group_score = 1 if market_segment == "Groups" else 0

    online_ta_score = 1 if market_segment == "Online TA" else 0

    score = (
        0.6 * lead_time_score(lead_time)
        + 0.2 * group_score
        + 0.2 * online_ta_score
    )

    return score * 100


def calculate_adjustment(
    demand_score,
    risk_score
):

    adjustment = (
        0.5
        * (
            (2 / 3) * (demand_score / 100)
            - (1 / 3) * (risk_score / 100)
        )
    ) * 100

    return adjustment


def recommend_adr(
    predicted_adr,
    demand_score,
    risk_score
):

    adjustment_pct = calculate_adjustment(
        demand_score,
        risk_score
    )

    recommended_adr = (
        predicted_adr
        * (1 + adjustment_pct / 100)
    )

    return round(recommended_adr, 2)


def predict_and_recommend(
    booking,
    rf,
    training_columns
):

    booking_df = pd.DataFrame([booking])

    booking_encoded = pd.get_dummies(
        booking_df,
        drop_first=True
    )

    booking_encoded = booking_encoded.reindex(
        columns=training_columns,
        fill_value=0
    )

    predicted_adr = rf.predict(
        booking_encoded
    )[0]

    demand_score = calculate_demand_score(
        booking["arrival_date_month"],
        booking["hotel"],
        booking["market_segment"]
    )

    risk_score = calculate_risk_score(
        booking["lead_time"],
        booking["market_segment"]
    )

    adjustment_pct = calculate_adjustment(
        demand_score,
        risk_score
    )

    recommended_adr = recommend_adr(
        predicted_adr,
        demand_score,
        risk_score
    )

    return {
        "Predicted ADR": round(predicted_adr, 2),
        "Demand Score": round(demand_score, 2),
        "Risk Score": round(risk_score, 2),
        "Adjustment %": round(adjustment_pct, 2),
        "Recommended ADR": round(recommended_adr, 2)
    }

    