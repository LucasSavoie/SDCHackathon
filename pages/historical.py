import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

def generate_chart(selected_options, start_year, end_year):
    df = pd.read_csv('emissions.csv')
    df2 = pd.read_csv('offsets.csv')

    # Store the number of industries in a variable to compute averages across all industries
    num_industries = len(df['Sector'])

    # Lists used to store year, and annual emission averages, and annual offset averages, and net-emissions
    years = []
    emission_averages = []
    offset_averages = []
    net_emissions = []

    # Calculate annual emissions averages across all industries/year
    for col in df.columns[1:]:
        # Extract year from header, add to appropriate list
        year = col[:4]
        if start_year <= int(year) <= end_year:  # Check if the year is within the selected range
            years.append(year)

            annual_total = df[col].sum() / num_industries  # Simplified sum calculation
            emission_averages.append(annual_total)

    # Calculate annual offset averages across all industries/year for the same range of years
    for col in df2.columns[1:]:
        year = col[:4]
        if year in years:
            annual_total = df2[col].sum() / num_industries  # Simplified sum calculation
            offset_averages.append(annual_total)

    # Calculate net-emission averages
    net_emissions = [emission_averages[i] - offset_averages[i] for i in range(min(len(emission_averages), len(offset_averages)))]

    # Plotting data
    fig, ax = plt.subplots(figsize=(8, 5))  # Create a subplot

    if "Emissions" in selected_options:
        plt.plot(years, emission_averages, marker='o', linestyle='-', color='b', label='Emission Averages')
    if "Offset" in selected_options:
        plt.plot(years, offset_averages, marker='o', linestyle='-', color='r', label='Offset Averages')
    if "Net" in selected_options:
        plt.plot(years, net_emissions, marker='o', linestyle='-', color='g', label='Net Emission Averages')

    # Adding labels and title
    plt.xlabel('Years')
    plt.ylabel('Averages')
    plt.title('Emission and Offset, and Net Emission Averages Over Years')

    # Adding legend
    plt.legend()

    # Displaying the plot
    plt.grid(True)
    plt.tight_layout()

    return fig  # Return the figure object


st.title('Irvine Oil Historical Data')

col1, col2, col3 = st.columns(3)
with col1:
   st.page_link("app.py", label="Home", icon="🏠")

with col2:
   st.page_link("pages/future.py", label="View Future Predictions")

with col3:
   st.page_link("pages/historical.py", label="View Histroical Data")

options = st.multiselect(
    "Select options", ['Emissions', 'Offset', 'Net'])

# Split the string and extract start and end years
years_str = st.slider(
    "Select the years",
    2013, 2023, (2013, 2023))

start_year, end_year = map(int, years_str)

fig = generate_chart(options, start_year, end_year)

st.pyplot(fig)