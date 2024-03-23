import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO



# Change the site title name
st.set_page_config(page_title="EnviroVision", page_icon="🌳")

left_co, cent_co, last_co = st.columns(3)

with cent_co:
    st.image('envirovision_logo.jpg',width= 200)

st.title('EnviroVision')

col1, col2, col3, col4 = st.columns(4)
with col1:
   st.page_link("app.py", label="**Home**", icon="🏠")

with col2:
   st.page_link("pages/future_costs.py", label="**View Future Predictions**")

with col3:
   st.page_link("pages/historical.py", label="**View Historical Data**")


with col4:
    st.page_link("pages/future.py", label="**Predicted Future Costs**")

st.markdown("""
    **Problem Description**
    The task is to design and implement an application for Irvine Gasoline, a large oil and gas company, aiming to transition to carbon neutrality after years of neglecting their carbon emissions. The application should assist Irvine Gasoline in managing and achieving their goal of becoming carbon neutral. 

    **How does EnviroVision solve this problem?**
    1. Analyzes previous carbon emission data, providing insights into historical environmental impact.
    2. By leveraging ML and predictive analytics, EnviroVision forecasts future emission trends, aiding Irvine Gasoline in setting achievable carbon neutrality goals.
    3. Additionally, EnviroVision offers tools for evaluating the effectiveness of different emission reduction strategies and selecting optimal carbon offsetting options.
""")

uploaded_file = st.file_uploader("**Input A File to Be Analyzed**")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


