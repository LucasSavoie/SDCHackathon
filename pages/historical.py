import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter
import pandas as pd
import numpy as np

# Change the site title name
st.set_page_config(page_title="EnviroVision", page_icon="🌳")

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

def generate_chart_sector(sector, selected_options, start_year, end_year):
    df1 = pd.read_csv("emissions.csv")
    df2 = pd.read_csv("offsets.csv")

    # Filter dataframes based on selected sector
    df1_sector = df1[df1['Sector'] == sector]
    df2_sector = df2[df2['Sector'] == sector]

    y = range(start_year, min(end_year + 1, 2014 + len(df1_sector.columns) - 1))  # Years range from start_year to the end of available data

    net = df1_sector.iloc[:, 1:].values - df2_sector.iloc[:, 1:].values
    emissions = df1_sector.iloc[:, 1:].values
    offsets = df2_sector.iloc[:, 1:].values

    plt.figure(figsize=(8, 5))
    plt.title(sector)
    plt.xlabel("Year")
    plt.ylabel("Tons of CO2")
    plt.grid(True, linestyle="-")
    if "Emissions" in selected_options:
        plt.plot(y, emissions[0][:len(y)], label="Emissions", color="b", marker="o")
    if "Offset" in selected_options: 
        plt.plot(y, offsets[0][:len(y)], label="Offsets", color="r", marker="o")
    if "Net" in selected_options:
        plt.plot(y, net[0][:len(y)], label="Net", color="g", marker="o")

    plt.legend(loc="upper right")
    
    return plt.gcf()  # Return the current figure

st.title('Irvine Oil Historical Data')

col1, col2, col3, col4 = st.columns(4)
with col1:
   st.page_link("app.py", label="**Home**", icon="🏠")

with col2:
   st.page_link("pages/future_costs.py", label="**View Future Predictions**")

with col3:
   st.page_link("pages/historical.py", label="**View Historical Data**")

with col4:
   st.page_link("pages/future.py", label="**Predicted Future Costs**")


options = st.multiselect(
    "Select options", ['Emissions', 'Offset', 'Net'])

sector = st.selectbox(
    'Select a Sector',
    ('All Sectors', 'Agriculture', 'Aviation', 'Commercial','Energy','Forestry',
    'Industrial','Marine','Residential','Transportation','Waste'))

# Split the string and extract start and end years
years_str = st.slider(
    "Select the years",
    2013, 2023, (2013, 2023))

start_year, end_year = map(int, years_str)

if sector == 'All Sectors':
    fig = generate_chart(options, start_year, end_year)
else:
    fig = generate_chart_sector(sector, options, start_year, end_year)
st.pyplot(fig)
