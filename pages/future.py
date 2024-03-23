import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)



st.title('Irvine Oil Future Predictions')

col1, col2, col3 = st.columns(3)
with col1:
   st.page_link("app.py", label="Home", icon="🏠")

with col2:
   st.page_link("pages/future.py", label="View Future Predictions")

with col3:
   st.page_link("pages/historical.py", label="View Histroical Data")



if st.button('View Chart'):
    st.pyplot(fig)


