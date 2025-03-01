import streamlit as st
import requests
from dotenv import load_dotenv
import os

# .env file load karein
load_dotenv()

# API Key environment variable se lein
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Streamlit UI
st.title("🌤 Weather App")
st.write("Enter a city name to check the weather!")
  
# User input
city = st.text_input("Enter city name", "Karachi")

# Weather fetch karne ka function
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            return {
                "City": city,
                "Temperature": f"{data['main']['temp']}°C",
                "Weather": data["weather"][0]["description"].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']} m/s"
            }
        except requests.exceptions.JSONDecodeError:
            return None
    else:
        st.error(f"❌ Error {response.status_code}: {response.text}")
        return None

# Button to fetch weather
if st.button("Get Weather"):
    weather_data = get_weather(city)

    if weather_data:
        st.success("✅ Weather data fetched successfully!")
        st.write(f"🌍 **City:** {weather_data['City']}")
        st.write(f"🌡 **Temperature:** {weather_data['Temperature']}")
        st.write(f"☁️ **Weather:** {weather_data['Weather']}")
        st.write(f"💧 **Humidity:** {weather_data['Humidity']}")
        st.write(f"🌬 **Wind Speed:** {weather_data['Wind Speed']}")
    else:
        st.error("❌ City not found or API issue. Please try again.")  







