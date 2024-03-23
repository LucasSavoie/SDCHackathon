import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Change the site title name
st.set_page_config(page_title="EnviroVision", page_icon="🌳")

st.title('Irvine Oil Future Predictions')

col1, col2, col3, col4 = st.columns(4)
with col1:
   st.page_link("app.py", label="**Home**", icon="🏠")

with col2:
   st.page_link("pages/future_costs.py", label="**View Future Predictions**")

with col3:
   st.page_link("pages/historical.py", label="**View Historical Data**")

with col4:
   st.page_link("pages/future.py", label="**Predicted Future Costs**")



