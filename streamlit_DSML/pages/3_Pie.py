import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.title("Pie Chart 🥧")

# Find the CSV file
csv_path = Path(__file__).resolve().parent.parent / "data" / "pie_demo.csv"

# Read the data
df = pd.read_csv(csv_path)

st.write("How Students Spend Their Free Time")

# Let users choose activities
activities = st.multiselect(
    "Select activities:",
    df["Activity"].tolist(),
    default=df["Activity"].tolist()
)

# Filter the selected activities
filtered_df = df[df["Activity"].isin(activities)]

# Create the pie chart
if not filtered_df.empty:
    fig = px.pie(
        filtered_df,
        names="Activity",
        values="Hours",
        title="How do students spend there free time"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please select an activity.")
