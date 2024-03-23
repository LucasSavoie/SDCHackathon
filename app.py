import streamlit as st
import matplotlib.pyplot as plt
import numpy as np



arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('Irving_Oil.svg.png',width= 150)

st.title('EnviroVision')

col1, col2, col3, col4 = st.columns(4)
with col1:
   st.page_link("app.py", label="Home", icon="🏠")

with col2:
   st.page_link("pages/future_costs.py", label="View Future Predictions")

with col3:
   st.page_link("pages/historical.py", label="View Histroical Data")

with col4:
    st.page_link("pages/future.py", label="Predicted Future Costs")

st.markdown("""
    **Problem Description**
    The task is to design and implement an application for Irvine Gasoline, a large oil and gas company, aiming to transition to carbon neutrality after years of neglecting their carbon emissions. The application should assist Irvine Gasoline in managing and achieving their goal of becoming carbon neutral. 

    **How does EnviroVision solve this problem?**
    1. Analyzes previous carbon emission data, providing insights into historical environmental impact.
    2. By leveraging ML and predictive analytics, EnviroVision forecasts future emission trends, aiding Irvine Gasoline in setting achievable carbon neutrality goals.
    3. Additionally, EnviroVision offers tools for evaluating the effectiveness of different emission reduction strategies and selecting optimal carbon offsetting options.
""")



