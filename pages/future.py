import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Change the site title name
st.set_page_config(page_title="EnviroVision", page_icon="🌳")

st.title('Future Purchases of Carbon Offsets')

col1, col2, col3, col4 = st.columns(4)
with col1:
   st.page_link("app.py", label="**Home**", icon="🏠")

with col2:
   st.page_link("pages/future_costs.py", label="**View Future Predictions**")

with col3:
   st.page_link("pages/historical.py", label="**View Historical Data**")

with col4:
   st.page_link("pages/future.py", label="**Predicted Future Costs**")

def generate_chart(selected_options):
    # Read the CSV file
    df = pd.read_csv('CarbonOffsetCompanies.csv')

    # Extract data from the DataFrame
    sectors = df['Sector']
    CO2OffsetTonnes = df['CO2OffsetTonnes']
    Cost = df['Cost']

    # Plotting data
    fig, ax = plt.subplots(figsize=(10, 6))  # Create a subplot

    if "CO2OffsetTonnes" in selected_options:
        plt.bar(sectors, CO2OffsetTonnes, color='b', label='CO2 Offset (Tonnes)')
    if "Cost" in selected_options:
        plt.bar(sectors, Cost, color='r', label='Cost')

    # Adding labels and title
    plt.xlabel('Sector')
    plt.ylabel('Values')
    plt.title('CO2 Offset Tonnes and Cost by Sector')

    # Adding legend
    plt.legend()

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Displaying the plot
    plt.grid(True)
    plt.tight_layout()

    return fig  # Return the figure object

# Example usage
selected_options = ['CO2OffsetTonnes', 'Cost']

percentage = st.slider(
    "Select your Ideal Carbon Emissions Reduction Percentage Range",
    0, 100, (0, 20))

botttom_end, top_end = map(int, percentage)

fig = generate_chart(selected_options)
st.pyplot(fig)


