import streamlit as st
import matplotlib.pyplot as plt
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

def generate_chart(selected_options, budget, goal):
    # Read the CSV file
    df = pd.read_csv('CarbonOffsetCompanies.csv')

    # Filter data based on sliders
    budget_range = (budget[0], budget[1])
    goal_range = (goal[0], goal[1])

    # Calculate the ratio of CO2 offset to cost
    df['Ratio'] = df['CO2OffsetTonnes'] / df['Cost']

    # Group by sector and select the row with the maximum ratio within each group
    best_options = df.loc[df.groupby('Sector')['Ratio'].idxmax()]

    # Filter data based on budget and goal range
    filtered_df = best_options[
        (best_options['Cost'] >= budget_range[0]) & 
        (best_options['Cost'] <= budget_range[1]) &
        (best_options['CO2OffsetTonnes'] >= goal_range[0]) & 
        (best_options['CO2OffsetTonnes'] <= goal_range[1])
    ]

    # Plotting data
    fig, ax = plt.subplots(figsize=(10, 6))  # Create a subplot

    if "CO2OffsetTonnes" in selected_options:
        bars1 = plt.bar(filtered_df['Sector'], filtered_df['CO2OffsetTonnes'], color='b', label='CO2 Offset (Tonnes)')
        for bar in bars1:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    if "Cost" in selected_options:
        bars2 = plt.bar(filtered_df['Sector'], filtered_df['Cost'], color='r', label='Cost')
        for bar in bars2:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

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
selected_options = st.multiselect(
    "Select data to display:",
    ['CO2OffsetTonnes', 'Cost'])

budget = st.slider(
    "Select your Ideal Budget Range ($)",
    0, 10000, (0, 10000))

goal = st.slider(
    "Select your Ideal Carbon Emissions Reduction Amount Range",
    0, 10000, (0, 10000))

fig = generate_chart(selected_options, budget, goal)
st.pyplot(fig)



