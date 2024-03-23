import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)



st.title(':evergreen_tree: Irvine Oil Historical Data :evergreen_tree:')


if st.button('View Chart'):
    st.pyplot(fig)


