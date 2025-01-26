import pandas as pd
import sqlite3
import numpy as np
import streamlit as st

@st.cache_data
def get_data():
    con = sqlite3.connect(r"D:\Projects\Data_sience\energy.db")
    df = pd.read_sql('''SELECT * FROM energy''', con)
    return df.set_index("Nation")

df = get_data()

countries = df["country"].unique()

st.title('Global energy metrics')
st.subheader('Raw data')

metrics_list = list(df.columns)
metrics_list.remove("Nation", "year")

metrics = st.multiselect("Select what data you would like to review.", list(metrics_list), "electricity_generation")

nations = st.multiselect("Choose countires"), list(countries), ["sweden"]

for i in metrics_list:
    data = df.loc[metrics_list[i]]
    data = data.loc[nations]
    data.plot(kind="line", x='year')
    
'''if not metrics:
       st.error("Please select at at least one metric")
else:
    data1 = df.loc[metrics]
    st.subheader

if not nations:
       st.error("Please select at at least one country")
else:
    data2 = df.loc[nations]
    st.subheader'''
    
