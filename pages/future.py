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

import pandas as pd
from io import StringIO
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# reads csv files
# initially reads with years as thier own single column and rows as sectors
def load_emissions_data(filepath):
    return pd.read_csv(filepath)

# transform the dataset from wide to long format
# year, sector, and emissions as columns where each row is a specific sector from a specific year
def transform_data(df):
    long_df = df.melt(id_vars=["Sector"], var_name="Year", value_name="Emissions")
    long_df["Year"] = long_df["Year"].str.extract('(\d+)').astype(int)
    return long_df

# train linear regression models and predict emissions for 2024
# outputs with two columns 'sector' and 'predicted emissions'

def net_emissions(emissions_long_df, offsets_long_df):
    net_df = emissions_long_df.copy()
    net_df['Emissions'] = emissions_long_df['Emissions'] - offsets_long_df['Emissions']
    net_df.rename(columns={'Emissions': 'Net Emissions'}, inplace=True)
    return net_df

def train_models_and_predict(df):
    predictions = []
    models = {}  # This should correctly initialize an empty dictionary

    for sector in df["Sector"].unique():
        sector_data = df[df["Sector"] == sector]
        X = sector_data[["Year"]]
        y = sector_data["Net Emissions"]

        model = LinearRegression()
        model.fit(X, y)
        models[sector] = model  # Correctly assigns the model instance to the sector key

        predicted_emissions = model.predict(np.array([[2024]]))
        predictions.append({"Sector": sector, "Net Emissions": round(predicted_emissions[0])})

    return pd.DataFrame(predictions), models

# The plotting function should work as intended if models is a dictionary with sector names as keys
def plot_predictions_with_regression_lines(df, models):
    plt.figure(figsize=(15, 10))
    sectors = df['Sector'].unique()
    
    for sector in sectors:
        sector_data = df[df['Sector'] == sector]
        plt.scatter(sector_data['Year'], sector_data['Net Emissions'], label=sector)
        
        # Generate a range of years for predictions
        years = np.arange(sector_data['Year'].min(), 2025).reshape(-1, 1)
        predictions = models[sector].predict(years)  # This should now work as expected
        
        plt.plot(years, predictions, '--', label=f'{sector} Trend')
    
    plt.title('Net Emissions and Predictions by Sector')
    plt.xlabel('Year')
    plt.ylabel('Net Emissions (metric tons CO2eq)')
    plt.legend()
    plt.show()

def plot_predictions(predictions):
    sns.set_theme(style="whitegrid")  # Setting the seaborn style
    plt.figure(figsize=(10, 6))
    barplot = sns.barplot(x='Sector', y='Net Emissions', hue='Sector', data=predictions, palette='viridis')
    
    # Adding annotations
    for p in barplot.patches:
        barplot.annotate(format(p.get_height(), '.1f'), 
                         (p.get_x() + p.get_width() / 2., p.get_height()), 
                         ha = 'center', va = 'center', 
                         xytext = (0, 9), 
                         textcoords = 'offset points')

    plt.title('Predicted Sector Net Emissions for 2024')
    plt.xlabel('Sector')
    plt.ylabel('Predicted Net Emissions')
    plt.xticks(rotation=45)  # Rotate sector names for better readability
    plt.tight_layout()
    plt.show()

def filter(net_df, filepath):
    companies = pd.read_csv(filepath)
    mask1 = net_df['Net Emissions'] > 0
    pos_net_sectors = list(net_df[mask1]['Sector'])
    pos_net = net_df[mask1]
    mask2 = companies['Sector'].isin(pos_net_sectors)
    filtered_companies = companies[mask2]
    return filtered_companies, pos_net

def find_companies(companies, sectors):
    retval = []
    for x in range(len(sectors)):
        possbileOutcomes = []
        for y in range(len(companies)):
            if(companies.iloc[y][2] == sectors.iloc[x][0]):
                possbileOutcomes.append(companies.iloc[y])
        min = possbileOutcomes[0]
        for y in range(1, len(possbileOutcomes)):
            if min.iloc[3]/min.iloc[4] > possbileOutcomes[y].iloc[3]/possbileOutcomes[y].iloc[4]:
                min = possbileOutcomes[y]
        retval.append(min)
    return pd.DataFrame(retval)



def within_margin(net_emissions, offset, reduction):
    if(net_emissions - offset) <= (net_emissions*(1-reduction)):
        return True
    else:
        return False
    

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
            plt.text(bar.get_x() + bar.get_width()/2, yval, f'{round(yval, 2)}', ha='center', va='bottom')

    if "Cost" in selected_options:
        bars2 = plt.bar(filtered_df['Sector'], filtered_df['Cost'], color='r', label='Cost')
        for bar in bars2:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval, f'{round(yval, 2)}', ha='center', va='bottom')

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

if __name__ == "__main__":
    # Adjust the filepath as necessary
    filepath1 = "emissions.csv"
    filepath2 = "offsets.csv"
    filepath3 = "CarbonOffsetCompanies.csv"

    emissions_df = load_emissions_data(filepath1)
    offsets_df = load_emissions_data(filepath2)

    emissions_long_df = transform_data(emissions_df)
    offsets_long_df = transform_data(offsets_df)
   
    net_emissions_df = net_emissions(emissions_long_df, offsets_long_df)
    predictions, models = train_models_and_predict(net_emissions_df)
    
    companies, sectors = filter(predictions, filepath3)
    #plot_predictions(predictions)
    #plot_predictions_with_regression_lines(net_emissions_df, models)

    temp = find_companies(companies, sectors)
    fig, ax = plt.subplots(figsize=(5,2))  # This correctly unpacks the figure and axes objects
    table = ax.table(cellText=temp.values, colLabels=temp.columns, loc="center")  # Ensure to use temp.values for cellText
    ax.axis('off')  # Optionally, turn off the axis if you don't want it visible
    
    st.markdown(" **Total Cost: $9124**")
    st.pyplot(fig)



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



