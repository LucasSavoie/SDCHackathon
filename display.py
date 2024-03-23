import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter
import pandas as pd
df = pd.read_csv("offsets.csv")
curFigure = 1
y = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
legendLoc = "upper right"
df1 = pd.read_csv("emissions.csv")
df2 = pd.read_csv("offsets.csv")
for x in df1.index:
    sector = df1['Sector'][x]
    data13 = df1['2013 (metric tons CO2eq)'][x] - \
        df2['2013 (metric tons CO2eq)'][x]
    data14 = df1['2014 (metric tons CO2eq)'][x] - \
        df2['2014 (metric tons CO2eq)'][x]
    data15 = df1['2015 (metric tons CO2eq)'][x] - \
        df2['2015 (metric tons CO2eq)'][x]
    data16 = df1['2016 (metric tons CO2eq)'][x] - \
        df2['2016 (metric tons CO2eq)'][x]
    data17 = df1['2017 (metric tons CO2eq)'][x] - \
        df2['2017 (metric tons CO2eq)'][x]
    data18 = df1['2018 (metric tons CO2eq)'][x] - \
        df2['2018 (metric tons CO2eq)'][x]
    data19 = df1['2019 (metric tons CO2eq)'][x] - \
        df2['2019 (metric tons CO2eq)'][x]
    data20 = df1['2020 (metric tons CO2eq)'][x] - \
        df2['2020 (metric tons CO2eq)'][x]
    data21 = df1['2021 (metric tons CO2eq)'][x] - \
        df2['2021 (metric tons CO2eq)'][x]
    data22 = df1['2022 (metric tons CO2eq)'][x] - \
        df2['2022 (metric tons CO2eq)'][x]
    data23 = df1['2023 (metric tons CO2eq)'][x] - \
        df2['2023 (metric tons CO2eq)'][x]
    net = [data13, data14, data15, data16, data17,
           data18, data19, data20, data21, data22, data23]
    data13 = df1['2013 (metric tons CO2eq)'][x]
    data14 = df1['2014 (metric tons CO2eq)'][x]
    data15 = df1['2015 (metric tons CO2eq)'][x]
    data16 = df1['2016 (metric tons CO2eq)'][x]
    data17 = df1['2017 (metric tons CO2eq)'][x]
    data18 = df1['2018 (metric tons CO2eq)'][x]
    data19 = df1['2019 (metric tons CO2eq)'][x]
    data20 = df1['2020 (metric tons CO2eq)'][x]
    data21 = df1['2021 (metric tons CO2eq)'][x]
    data22 = df1['2022 (metric tons CO2eq)'][x]
    data23 = df1['2023 (metric tons CO2eq)'][x]
    emissions = [data13, data14, data15, data16, data17,
                 data18, data19, data20, data21, data22, data23]
    data13 = df2['2013 (metric tons CO2eq)'][x]
    data14 = df2['2014 (metric tons CO2eq)'][x]
    data15 = df2['2015 (metric tons CO2eq)'][x]
    data16 = df2['2016 (metric tons CO2eq)'][x]
    data17 = df2['2017 (metric tons CO2eq)'][x]
    data18 = df2['2018 (metric tons CO2eq)'][x]
    data19 = df2['2019 (metric tons CO2eq)'][x]
    data20 = df2['2020 (metric tons CO2eq)'][x]
    data21 = df2['2021 (metric tons CO2eq)'][x]
    data22 = df2['2022 (metric tons CO2eq)'][x]
    data23 = df2['2023 (metric tons CO2eq)'][x]
    offsets = [data13, data14, data15, data16, data17,
               data18, data19, data20, data21, data22, data23]
    plt.figure(curFigure)
    plt.title(str(sector))
    plt.xlabel("Year")
    plt.ylabel("Tons of C02")
    ax = plt.subplot()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_major_formatter(ScalarFormatter())
    plt.grid(True, linestyle="-")
    plt.plot(y, emissions, label="Emissions", color="b", marker="o")
    plt.plot(y, offsets, label="Offsets", color="r", marker="o")
    plt.plot(y, net, label="Net", color="g", marker="o")
    plt.legend(loc=legendLoc)
    curFigure += 1
plt.show()
