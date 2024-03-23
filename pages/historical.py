import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)



st.title(':evergreen_tree: Irvine Carbon Challenge :evergreen_tree:')

st.page_link("app.py", label="Home", icon="🏠")
st.page_link("historical.py", label="Page 1", icon="1️⃣")


if st.button('View Chart'):
    st.pyplot(fig)


