import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st  # Import Streamlit library

# Define functions for data loading, transformation, prediction, and plotting

def load_emissions_data(filepath):
    return pd.read_csv(filepath)

def transform_data(df):
    long_df = df.melt(id_vars=["Sector"], var_name="Year", value_name="Emissions")
    long_df["Year"] = long_df["Year"].str.extract('(\d+)').astype(int)
    return long_df

def net_emissions(emissions_long_df, offsets_long_df):
    net_df = emissions_long_df.copy()
    net_df['Emissions'] = emissions_long_df['Emissions'] - offsets_long_df['Emissions']
    return net_df

def train_models_and_predict(df):
    predictions = []
    models = {}

    for sector in df["Sector"].unique():
        sector_data = df[df["Sector"] == sector]
        X = sector_data[["Year"]]
        y = sector_data["Emissions"]

        model = LinearRegression()
        model.fit(X, y)
        models[sector] = model

        predicted_emissions = model.predict(np.array([[2024]]))
        predictions.append({"Sector": sector, "Emissions": round(predicted_emissions[0])})

    return pd.DataFrame(predictions), models

def plot_predictions_with_regression_lines(df, models):
    plt.figure(figsize=(15, 10))
    sectors = df['Sector'].unique()
    
    for sector in sectors:
        sector_data = df[df['Sector'] == sector]
        plt.scatter(sector_data['Year'], sector_data['Emissions'], label=sector)
        
        years = np.arange(sector_data['Year'].min(), 2025).reshape(-1, 1)
        predictions = models[sector].predict(years)
        
        plt.plot(years, predictions, '--', label=f'{sector} Trend')
    
    plt.title('Emissions and Predictions by Sector')
    plt.xlabel('Year')
    plt.ylabel('Emissions (metric tons CO2eq)')
    plt.legend()
    plt.tight_layout()
    return plt.gcf()  # Return the current figure

def plot_predictions(predictions):
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    barplot = sns.barplot(x='Sector', y='Emissions', hue='Sector', data=predictions, palette='viridis')
    
    for p in barplot.patches:
        barplot.annotate(format(p.get_height(), '.1f'), 
                         (p.get_x() + p.get_width() / 2., p.get_height()), 
                         ha = 'center', va = 'center', 
                         xytext = (0, 9), 
                         textcoords = 'offset points')

    plt.title('Predicted Sector Emissions for 2024')
    plt.xlabel('Sector')
    plt.ylabel('Predicted Emissions')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()  # Return the current figure

if __name__ == "__main__":
    filepath1 = "emissions.csv"
    filepath2 = "offsets.csv"

    emissions_df = load_emissions_data(filepath1)
    offsets_df = load_emissions_data(filepath2)

    emissions_long_df = transform_data(emissions_df)
    offsets_long_df = transform_data(offsets_df)
   
    net_emissions_df = net_emissions(emissions_long_df, offsets_long_df)
    predictions, models = train_models_and_predict(net_emissions_df)

    # Display the graphs using Streamlit
    st.title('Predicted Emissions')
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.page_link("app.py", label="Home", icon="🏠")

    with col2:
        st.page_link("pages/future_costs.py", label="View Future Predictions")

    with col3:
        st.page_link("pages/historical.py", label="View Histroical Data")

    with col4:
        st.page_link("pages/future.py", label="Predicted Future Costs")

    st.pyplot(plot_predictions(predictions))

    st.title('Emissions and Predictions by Sector')
    st.pyplot(plot_predictions_with_regression_lines(net_emissions_df, models))
