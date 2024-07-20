import streamlit as st
import plotly.express as px

# Add widgets
st.title("Weather Forecast for Next Days")
city = st.text_input("Place:")
days = st.slider("Forecast Days: ", min_value=1, max_value=5,
                 help="Choose the number of forecast days.")

option = st.selectbox("Select data to view: ",
                      options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {city}")

# Get data
def get_data():
    dates = ["2024-19-7", "2024-20-7", "2024-21-7"]
    temperatures = [23, 20, 29]
    return dates, temperatures


d, t = get_data()

# Create a plot
figure = px.line(x=d, y=t, labels={'x': "Date", 'y': "Temperature"})
st.plotly_chart(figure)
