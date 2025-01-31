# Importing modules.

import pandas as pd
import sqlite3
import numpy as np
import streamlit as st

# Retriving and cashing the data from the database.

@st.cache_data
def get_data():
    con = sqlite3.connect(r"C:\Users\user1\Documents\School\TUC\data_sience\tasks\energy.db")
    df = pd.read_sql('''SELECT * FROM energy''', con)
    return df
df = get_data()

countries = df["country"].unique()

st.title('Global energy metrics')

metrics_list = list(df.columns)
metrics_list.remove("country")
metrics_list.remove("year")
metrics_list.remove("index")

# Selecing what data to view

metrics = st.multiselect("Select what data you would like to review.", list(metrics_list), "electricity_generation")

if not metrics:
       st.error("Please select at at least one metric")
else:
    pass

# Selecting what nations to view.

nations = st.multiselect("Choose countires", list(countries), ["Sweden", "Japan"])

if not nations:
       st.error("Please select at at least one country")
else:
    pass

# Creating a dataframe contianing selected data

filtered_data = df[df["country"].isin(nations)]

# Loop through selected metrics and plot the data
for metric in metrics:
    st.subheader(f"{metric}")
    metric_data = filtered_data[["year", "country", metric]]
    metric_data = metric_data.set_index("year")
    st.line_chart(metric_data.pivot(columns="country", values=metric))
    
st.subheader('Raw data')
st.write(df)