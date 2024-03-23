import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
import pandas as pd 

#annual carbon emissions across all sectors
#create dataframe to store emission data, and offset data
df = pd.read_csv('emissions.csv')
df2 = pd.read_csv('offsets.csv')

#store the number of industires in a variable to compute averages across all industries
num_industries = len(df['Sector'])

#lists used to store year, and annual emission averages, and annual offset averages, and net-emissions
years = []
emission_averages = []
offset_averages = []
net_emissions = []

#calculate annual emissions averages across all industries/year
for col in df.columns[1:]:

    #extract year from header, add to appropriate list
    year = col[0:5]
    years.append(year)

    annual_total = 0
    #loop through and sum emmisions
    for entry in df[col]:
        annual_total += entry
        
    #divide annual total by number of industries to get annual average (emissions)
    annual_total = annual_total/num_industries
    emission_averages.append(annual_total)

annual_total = 0

#calculate annual offset averages across all industries/year
for col in df2.columns[1:]:

    #loop through and sum offsets
    for entry in df2[col]:
        annual_total += entry
        
    #divide annual total by number of industries to get annual average (offsets)
    annual_total = annual_total/num_industries
    offset_averages.append(annual_total)

#calculate net-emission averages
net_emissions = [emission_averages[i] - offset_averages[i] for i in range(min(len(emission_averages), len(offset_averages)))]

plt.plot(years, emission_averages, marker='o', linestyle='-', color='b', label='Emission Averages')
plt.plot(years, offset_averages, marker='o', linestyle='-', color='r', label='Offset Averages')
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
plt.show()

        

        
        


