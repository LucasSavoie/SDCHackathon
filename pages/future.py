import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)



st.title('Irvine Oil Future Predictions')

st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/future.py", label="View Future Predictions")
st.page_link("pages/historical.py", label="View Histroical Data")



if st.button('View Chart'):
    st.pyplot(fig)


