# 🏨 Dynamic Hotel Pricing Engine

## 🚀 Live Demo

🔗 **[Try the Application](https://dynamic-pricing-engine-vinit-bodhe.streamlit.app/)**


🔗  [LinkedIn](www.linkedin.com/in/vinitsbodhe)

---

## Overview

Traditional hotel pricing strategies often rely on static pricing rules that fail to account for changing demand patterns and cancellation risks. This project addresses that challenge by combining Machine Learning and business-driven pricing logic to generate dynamic room rate recommendations.

The solution predicts the Average Daily Rate (ADR) using historical booking data and further adjusts the predicted price using a custom demand and cancellation-risk scoring framework.

---

## Problem Statement

Hotels frequently struggle with:

* Static room pricing
* Seasonal demand fluctuations
* High cancellation rates
* Revenue leakage from underpriced inventory

The goal of this project is to develop a Dynamic Pricing Engine that recommends optimized room rates based on booking characteristics and market conditions.

---

## Dataset

* Hotel Booking Demand Dataset   [Link](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)
* 119,000+ hotel booking records
* Features include:

  * Hotel Type
  * Arrival Month
  * Market Segment
  * Lead Time
  * Adults, Children, Babies
  * Previous Cancellations
  * Booking Changes
  * Customer Type

---

## Project Workflow

```text
Data Collection
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Random Forest Regression
        ↓
ADR Prediction
        ↓
Demand Scoring
        ↓
Cancellation Risk Scoring
        ↓
Dynamic Pricing Recommendation
```

---

## Exploratory Data Analysis Highlights

### Demand Insights

* August, July, and May showed the highest booking demand.
* City Hotels received nearly 2× the bookings of Resort Hotels.
* Online Travel Agencies (Online TA) generated the highest booking volume.

### Cancellation Insights

* Cancellation rates increased significantly with longer lead times.
* Group bookings exhibited elevated cancellation behavior.
* Online TA bookings showed higher cancellation rates compared to Direct bookings.

---

## Machine Learning Model

### Algorithm

Random Forest Regressor

### Performance

* R² Score: **0.69**
* MAE: **17.43**
* RMSE: **26.13**


The model predicts the baseline ADR for a booking using booking and customer characteristics.

---

## Dynamic Pricing Engine

A custom pricing engine was developed on top of the machine learning model.

### Demand Score Factors

* Seasonality (Month)
* Hotel Type
* Booking Platform

### Cancellation Risk Factors

* Lead Time
* Group Bookings
* Online TA Bookings

### Pricing Logic

```text
Predicted ADR
        ↓
Demand Score
        ↓
Risk Score
        ↓
Adjustment Percentage
        ↓
Recommended ADR
```

The engine can dynamically adjust room prices by up to approximately ±33% depending on demand and risk conditions.

---

## Streamlit Application

The project includes an interactive Streamlit dashboard where users can:

* Select booking characteristics
* Predict ADR
* View Demand Score
* View Risk Score
* View Adjustment Percentage
* Receive Recommended ADR

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib

---

## Project Structure

```text
Dynamic Engine/
│
├── models/
│   ├── hotel_pricing_model.pkl
│   └── training_columns.pkl
│
├── src/
│   ├── pricing_engine.py
│   └── __init__.py
│
├── app.py
├── requirements.txt
├── README.md
└── hotel_pricing_eda.ipynb
```

---

## Future Improvements

* Real-time occupancy integration
* Competitor price monitoring
* Revenue optimization using reinforcement learning
* Automated demand forecasting
* Cloud deployment and API integration

---

## Author

Vinit Bodhe

Built as a Data Analytics & Machine Learning project demonstrating predictive modeling, business problem-solving, and dynamic pricing strategy design.
