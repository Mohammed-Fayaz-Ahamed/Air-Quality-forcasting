# ~ ~ ~ ~ ~ ~ ~ ~  OM SHRI GANESHAAYA NAMAHA ~ ~ ~ ~ ~ ~ ~ ~ 

import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('forecast_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create a Streamlit app
st.title("CO2 Emissions Forecasting")
st.write("Forecast CO2 emissions for a given number of years")

# UI elements
years_to_forecast = st.number_input("Enter the number of years to forecast:", min_value=1, max_value=100)

# Function to run the model
def forecast(years):
    forecast_data = model.forecast(years)
    return forecast_data

# Visualize the results
forecast_data = forecast(years_to_forecast)
st.line_chart(forecast_data)