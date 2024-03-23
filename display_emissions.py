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

# Plotting
fig, ax = plt.subplots()
lines = []
labels = []

def plot_data():
    global lines, labels
    lines = []
    labels = []
    if emission_visible:
        lines.append(ax.plot(years, emission_averages, marker='o', linestyle='-', color='b')[0])
        labels.append('Emission Averages')
    if offset_visible:
        lines.append(ax.plot(years, offset_averages, marker='o', linestyle='-', color='r')[0])
        labels.append('Offset Averages')
    if net_visible:
        lines.append(ax.plot(years, net_emissions, marker='o', linestyle='-', color='g')[0])
        labels.append('Net Emission Averages')
    ax.legend(lines, labels, loc='upper left')

# Initial visibility state
emission_visible = True
offset_visible = True
net_visible = True
plot_data()

# Adding labels and title
ax.set_xlabel('Years')
ax.set_ylabel('Averages')
ax.set_title('Emission, Offset, and Net Emission Averages Over Years')

# Create checkboxes
rax = plt.axes([0.85, 0.4, 0.1, 0.2])
check = CheckButtons(rax, ('Emission', 'Offset', 'Net Emission'), (emission_visible, offset_visible, net_visible))

# Toggle function
def toggle_visibility(label):
    global emission_visible, offset_visible, net_visible
    if label == 'Emission':
        emission_visible = not emission_visible
    elif label == 'Offset':
        offset_visible = not offset_visible
    elif label == 'Net Emission':
        net_visible = not net_visible
    ax.clear()
    plot_data()
    plt.draw()

check.on_clicked(toggle_visibility)

# Displaying the plot
plt.grid(True)
plt.tight_layout()
plt.show()

        
        


