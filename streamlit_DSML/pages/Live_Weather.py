import streamlit as st
import pandas as pd
import requests
import plotly.express as px

lat, lon = 39.7392, -104.9903  # Denver
wurl = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
@st.cache_data(ttl=600)
def get_weather():
    r = requests.get(wurl, timeout=10); r.raise_for_status()
    j = r.json()["current"]
    return pd.DataFrame([{"time": pd.to_datetime(j["time"]),
                          "temperature": j["temperature_2m"],
                          "wind": j["wind_speed_10m"]}])

st.title("Denver Temperature Over Time")

df = get_weather()

# Keep a history of temperature readings
if "weather_history" not in st.session_state:
    st.session_state.weather_history = pd.DataFrame(
        columns=["time", "temperature", "wind"]
    )

st.session_state.weather_history = pd.concat(
    [st.session_state.weather_history, df],
    ignore_index=True
)

st.session_state.weather_history = (
    st.session_state.weather_history
    .drop_duplicates(subset=["time"], keep="last")
    .sort_values("time")
    .tail(60)
)

df = st.session_state.weather_history

st.dataframe(df, use_container_width=True)

fig = px.line(df, x="time", y="temperature",
              title="Denver Temperature Over Time",
              markers=True)

st.plotly_chart(fig, use_container_width=True)
