import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Energy Forecasting Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_url ="/Users/hrishikeshhpillai/Documents/hrishi/deeplearning/gridai/forecasting/datasets/SolarPrediction2.csv"


# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url, parse_dates=['datetime'])

df = get_data()

# dashboard title
st.title("Real time Energy Forecasting Dashboard")

# top-level filters
state = st.selectbox("Select the district", ['Ernankulam', 'Kottayam', 'Trivandrum', 'Kollam', 'Thrissur', 'Palakkad', 'Kozhikode', 'Malappuram', 'Kannur', 'Kasaragod'])

# creating a single-element container
placeholder = st.empty()

# dataframe filter
# df = df[df["state"] == state]

# Radiation	Temperature	Pressure	Humidity	WindDirection(Degrees)	Speed

# near real-time / live feed simulation
for seconds in range(200):

    df["Radiation_new"] = df["Radiation"] * np.random.choice(range(1, 5))
    df["Temperature_new"] = df["Temperature"] * np.random.choice(range(1, 5))
    df["Pressure_new"] = df["Pressure"] * np.random.choice(range(1, 5))
    df["Humidity_new"] = df["Humidity"] * np.random.choice(range(1, 5))
    df["WindDirection(Degrees)_new"] = df["WindDirection(Degrees)"] * np.random.choice(range(1, 5))
    df["Speed_new"] = df["Speed"] * np.random.choice(range(1, 5))
    

    # creating KPIs
    
    # avg_age = np.mean(df["age_new"])
    
    avg_radiation = np.mean(df["Radiation_new"])
    avg_temperature = np.mean(df["Temperature_new"])
    avg_pressure = np.mean(df["Pressure_new"])
    avg_humidity = np.mean(df["Humidity_new"])
    avg_winddirection = np.mean(df["WindDirection(Degrees)_new"])
    avg_speed = np.mean(df["Speed_new"])





    with placeholder.container():


        kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)


        kpi1.metric(
            label="Radiation",
            value=round(avg_radiation),
            delta=round(avg_radiation) - 10,
        )

        kpi2.metric(
            label="Temperature",
            value=round(avg_temperature),
            delta=round(avg_temperature) - 10,
        )

        kpi3.metric(
            label="Pressure",
            value=round(avg_pressure),
            delta=round(avg_pressure) - 10,
        )

        kpi4.metric(
            label="Humidity",
            value=round(avg_humidity),
            delta=round(avg_humidity) - 10,
        )

        kpi5.metric(
            label="WindDirection(Degrees)",
            value=round(avg_winddirection),
            delta=round(avg_winddirection) - 10,
        )

        kpi6.metric(
            label="Speed",
            value=round(avg_speed),
            delta=round(avg_speed) - 10,
        )

        st.markdown("## Insights")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.text_area(
                label="Radiation",
                value="The average radiation is increasing by 10% compared to the previous year"
            )
        with col2:
            st.text_area(
                label="Tempreature",
                value="The average temperature is increasing by 10% compared to the previous year"
            )
        with col3:
        # increase font size
            st.text_area(
                label="Pressure",
                value="The average pressure is increasing by 10% compared to the previous year"
            )

        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        # with fig_col1:
        #     st.markdown("### First Chart")
        #     fig = px.density_heatmap(
        #         data_frame=df, y="age_new", x="marital"
        #     )
        #     st.write(fig)

        #time series chart for radiation
        with fig_col1:
            st.markdown("### Radiation Chart")
            fig = px.line(
                data_frame=df, y="Radiation_new", x="datetime"
            )
            st.write(fig)
            
        #time series chart for temperature

        with fig_col2:
            st.markdown("### Tempereture Chart")
            fig = px.line(
                data_frame=df, y="Temperature_new", x="datetime"
            )
            st.write(fig)

        st.markdown("### Detailed Data View")
        st.dataframe(df)

        # st.button("Load Shedding")

        
        
        time.sleep(1)
