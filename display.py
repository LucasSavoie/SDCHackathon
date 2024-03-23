import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter
import numpy as np
import pandas as pd
from matplotlib.widgets import CheckButtons
df = pd.read_csv("offsets.csv")
curFigure = 1
y = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

for x in df.index:
    sector = df['Sector'][x]
    data13 = df['2013 (metric tons CO2eq)'][x]
    data14 = df['2014 (metric tons CO2eq)'][x]
    data15 = df['2015 (metric tons CO2eq)'][x]
    data16 = df['2016 (metric tons CO2eq)'][x]
    data17 = df['2017 (metric tons CO2eq)'][x]
    data18 = df['2018 (metric tons CO2eq)'][x]
    data19 = df['2019 (metric tons CO2eq)'][x]
    data20 = df['2020 (metric tons CO2eq)'][x]
    data21 = df['2021 (metric tons CO2eq)'][x]
    data22 = df['2022 (metric tons CO2eq)'][x]
    data23 = df['2023 (metric tons CO2eq)'][x]
    x = [data13, data14, data15, data16, data17,
         data18, data19, data20, data21, data22, data23]
    plt.figure(curFigure)
    plt.title(str(sector) + " offset")
    plt.xlabel("Year")
    plt.ylabel("Offset (tons of C02)")
    ax = plt.subplot()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_major_formatter(ScalarFormatter())
    plt.grid(True, linestyle="-")
    curFigure += 1
    plt.plot(y, x)
df = pd.read_csv("emissions.csv")
for x in df.index:
    sector = df['Sector'][x]
    data13 = df['2013 (metric tons CO2eq)'][x]
    data14 = df['2014 (metric tons CO2eq)'][x]
    data15 = df['2015 (metric tons CO2eq)'][x]
    data16 = df['2016 (metric tons CO2eq)'][x]
    data17 = df['2017 (metric tons CO2eq)'][x]
    data18 = df['2018 (metric tons CO2eq)'][x]
    data19 = df['2019 (metric tons CO2eq)'][x]
    data20 = df['2020 (metric tons CO2eq)'][x]
    data21 = df['2021 (metric tons CO2eq)'][x]
    data22 = df['2022 (metric tons CO2eq)'][x]
    data23 = df['2023 (metric tons CO2eq)'][x]
    x = [data13, data14, data15, data16, data17,
         data18, data19, data20, data21, data22, data23]
    plt.figure(curFigure)
    plt.title(str(sector) + " emissions")
    plt.xlabel("Year")
    plt.ylabel("Offset (tons of C02)")
    ax = plt.subplot()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_major_formatter(ScalarFormatter())
    plt.grid(True, linestyle="-")
    curFigure += 1
    plt.plot(y, x)
df1 = pd.read_csv("emissions.csv")
df2 = pd.read_csv("offsets.csv")
for x in df.index:
    sector = df['Sector'][x]
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
    x = [data13, data14, data15, data16, data17,
         data18, data19, data20, data21, data22, data23]
    plt.figure(curFigure)
    plt.title(str(sector) + " net")
    plt.xlabel("Year")
    plt.ylabel("Offset (tons of C02)")
    ax = plt.subplot()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_major_formatter(ScalarFormatter())
    plt.grid(True, linestyle="-")
    curFigure += 1
    plt.plot(y, x)

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
    curFigure += 1
    plt.plot(y, emissions, label="emissions")
    plt.plot(y, offsets, label="offsets")
    plt.plot(y, net, label="net")
    plt.legend()
plt.show()
