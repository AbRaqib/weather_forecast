import streamlit as st
import plotly.express as px
from backend import get_data

# Add widgets
st.title("Weather Forecast for Next Days")
city = st.text_input("Place:")
days = st.slider("Forecast Days: ", min_value=1
                 , max_value=5,
                 help="Choose the number of forecast days.")

option = st.selectbox("Select data to view: ",
                      options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {city}")

# Get data
data = get_data(city, days, option)

# Create a plot
figure = px.line(x=d, y=t, labels={'x': "Date", 'y': "Temperature"})
st.plotly_chart(figure)
