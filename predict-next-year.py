import pandas as pd
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
def train_models_and_predict(df):
    predictions = []
    models = {}  # This should correctly initialize an empty dictionary

    for sector in df["Sector"].unique():
        sector_data = df[df["Sector"] == sector]
        X = sector_data[["Year"]]
        y = sector_data["Emissions"]

        model = LinearRegression()
        model.fit(X, y)
        models[sector] = model  # Correctly assigns the model instance to the sector key

        predicted_emissions = model.predict(np.array([[2024]]))
        predictions.append({"Sector": sector, "Emissions": round(predicted_emissions[0])})

    return pd.DataFrame(predictions), models

# The plotting function should work as intended if models is a dictionary with sector names as keys
def plot_predictions_with_regression_lines(df, models):
    plt.figure(figsize=(15, 10))
    sectors = df['Sector'].unique()
    
    for sector in sectors:
        sector_data = df[df['Sector'] == sector]
        plt.scatter(sector_data['Year'], sector_data['Emissions'], label=sector)
        
        # Generate a range of years for predictions
        years = np.arange(sector_data['Year'].min(), 2025).reshape(-1, 1)
        predictions = models[sector].predict(years)  # This should now work as expected
        
        plt.plot(years, predictions, '--', label=f'{sector} Trend')
    
    plt.title('Emissions and Predictions by Sector')
    plt.xlabel('Year')
    plt.ylabel('Emissions (metric tons CO2eq)')
    plt.legend()
    plt.show()

def plot_predictions(predictions):
    sns.set_theme(style="whitegrid")  # Setting the seaborn style
    plt.figure(figsize=(10, 6))
    barplot = sns.barplot(x='Sector', y='Emissions', hue='Sector', data=predictions, palette='viridis')
    
    # Adding annotations
    for p in barplot.patches:
        barplot.annotate(format(p.get_height(), '.1f'), 
                         (p.get_x() + p.get_width() / 2., p.get_height()), 
                         ha = 'center', va = 'center', 
                         xytext = (0, 9), 
                         textcoords = 'offset points')

    plt.title('Predicted Sector Emissions for 2024')
    plt.xlabel('Sector')
    plt.ylabel('Predicted Emissions')
    plt.xticks(rotation=45)  # Rotate sector names for better readability
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Adjust the filepath as necessary
    filepath = 'emissions.csv'
    emissions_df = load_emissions_data(filepath)
    emissions_long_df = transform_data(emissions_df)
    predictions, models = train_models_and_predict(emissions_long_df)

    plot_predictions_with_regression_lines(emissions_long_df, models)
    plot_predictions(predictions)



