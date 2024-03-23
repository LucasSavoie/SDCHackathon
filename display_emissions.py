import matplotlib.pyplot as plt
import pandas as pd 

#annual carbon emissions across all sectors
#create dataframe to store emission data
df = pd.read_csv('emissions.csv')

#store the number of industires in a variable to compute averages across all industries
num_industries = len(df['Sector'])

#lists used to store year, and annual emission averages
years = []
emission_averages = []

#sum annual emissions across all industries
for col in df.columns[1:]:

    #extract year from header, add to appropriate list
    year = col[0:5]
    years.append(year)

    annual_total = 0
    #loop through and sum emmisions
    for entry in df[col]:
        annual_total += entry
        
    #divide annual total by number of industries to get annual average
    annual_total = annual_total/num_industries
    emission_averages.append(annual_total)

#plotting data
plt.plot(years, emission_averages, marker='o', linestyle='-')

#adding labels and title
plt.xlabel('Years')
plt.ylabel('Emission Average')
plt.title('Yearly Emission Averages')

#display the plot
plt.grid(True)
plt.show()

#sector
    

        

        
        


