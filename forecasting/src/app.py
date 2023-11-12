import time 

import numpy as np  
import pandas as pd  
import plotly.express as px  
import streamlit as st 
import random

st.set_page_config(
    page_title="Energy Forecasting Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_url ="../datasets/SolarPrediction2.csv"


# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url, parse_dates=['datetime'])

df1 = get_data()



# dashboard title
st.title(":red[GridNet AI]")

# top-level filters
state = st.selectbox("Select the district", ['Ernankulam', 'Kottayam', 'Trivandrum', 'Kollam', 'Thrissur', 'Palakkad', 'Kozhikode', 'Malappuram', 'Kannur', 'Kasaragod'])

# creating a single-element container
placeholder = st.empty()





i = random.randint(0, len(df1)-7)


df = df1[i:i+7]


df["Radiation_new"] = df["Radiation"] * np.random.choice(range(1, 5))
df["Temperature_new"] = df["Temperature"] * np.random.choice(range(1, 5))
df["Pressure_new"] = df["Pressure"] * np.random.choice(range(1, 5))
df["Humidity_new"] = df["Humidity"] * np.random.choice(range(1, 5))
df["WindDirection(Degrees)_new"] = df["WindDirection(Degrees)"] * np.random.choice(range(1, 5))
df["Speed_new"] = df["Speed"] * np.random.choice(range(1, 5))


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
        value=f"{round(avg_radiation)} W/m\u00b2",
        delta=round(avg_radiation) - 10,
    )

    kpi2.metric(
        label="Temperature",
        value=f"{round(avg_temperature)} °F",
        delta=round(avg_temperature) - 10,
    )

    kpi3.metric(
        label="Pressure",
        value=f"{round(avg_pressure)} Pa",
        delta=round(avg_pressure) - 10,
    )

    kpi4.metric(
        label="Humidity",
        value=f"{round(avg_humidity)} g/m\u00b3",
        delta=round(avg_humidity) - 10,
    )

    kpi5.metric(
        label="WindDirection(Degrees)",
        value=f"{round(avg_winddirection)} ° ",
        delta=round(avg_winddirection) - 10,
    )

    kpi6.metric(
        label="Speed",
        value=f"{round(avg_speed)} km/hr",
        delta=round(avg_speed) - 10,
    )






    st.button("Update Values")

    st.markdown("## Forecasted Values")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("#### Forecasted Generation")
        st.title(":red[1000 KwHr]")

        


    with c2:

        st.markdown("#### Forecasted Load")

        st.title(":green[1000 KwHr]")

    st.markdown("## Insights")

    
    
    st.text_area(
        label="### Radiation",
        value="The average radiation is increasing by 10% compared to the previous year"
    )
   

    

   
    
    

    

    

    # create two columns for charts
    fig_col1, fig_col2 = st.columns(2)
   
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
