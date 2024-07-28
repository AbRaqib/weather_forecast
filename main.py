import streamlit as st
import plotly.express as px
from backend import get_data

# Add widgets
st.info("Created by Abdul Raqib 'Ramaki'")
st.title("Weather Forecast for Next Days")
city = st.text_input("Place:")
days = st.slider("Forecast Days: ", min_value=1, max_value=5,
                 help="Choose the number of forecast days.")
option = st.selectbox("Select data to view: ",
                      options=("Temperature", "Sky"))
try:
    st.subheader(f"{option} for the next {days} days in {city}")

    if city:
        # Get data
        filtered_data = get_data(city, days)

        # Create a plot for temperature
        if option == "Temperature":
            temperatures = [dic['main']['temp'] / 10 for dic in filtered_data]
            times = [dic['dt_txt'] for dic in filtered_data]
            figure = px.line(x=times, y=temperatures,
                             labels={'x': "Date", 'y': "Temperature"})
            st.plotly_chart(figure)

        # Render images for sky condition
        if option == "Sky":
            sky_conditions = [dic['weather'][0]['main'] for dic in filtered_data]
            translation = {'Clear': 'images/clear.png', 'Rain': 'images/rain.png',
                           'Snow': 'images/snow.png', 'Clouds': 'images/cloud.png'}
            image_paths = [translation[condition] for condition in sky_conditions]
            st.image(image_paths, width=100)
except KeyError:
    st.info("Oops! You entered an non-existing city name.")