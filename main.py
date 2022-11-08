
import numpy

import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm

df = pd.read_csv("/Users/jonathannaumanen/Downloads/life-expectancy-vs-gdp-per-capita.csv")

data_18 = df[df['Year'] == 2018]
data_pop = data_18[data_18['Population (historical estimates)'] > 1000000]
data_pop_higher_gdp_than_14 = data_pop[data_pop['GDP per capita'] > 140000]
print("Countries with population higher than 1 million and GDP per capita higher than 140000: ", data_pop_higher_gdp_than_14['Entity'].unique())
data_pop_lower_than_14_GDP = data_pop[data_pop['GDP per capita'] < 140000]
yValues = data_pop_lower_than_14_GDP['Life expectancy']
xValues = data_pop_lower_than_14_GDP['GDP per capita']
plt.xlabel('GDP per capita')
plt.ylabel('Life expectancy')
plt.scatter(xValues, yValues, edgecolors='black', linewidths=0.5, s=25)
plt.show()
data_world = data_pop[data_pop['Entity'] == 'World']
life_expectancy_world = data_world['Life expectancy']
life_expectancy_world_sum = life_expectancy_world.sum()
gdp_world = data_world['GDP per capita']
gdp_world_sum = gdp_world.sum()
data_not_world = data_pop[data_pop['Entity'] != 'World']
life_expectancy_not_world = data_not_world['Life expectancy']
n = life_expectancy_not_world.size
list_life_expectancy_not_world = life_expectancy_not_world.tolist()

print(list_life_expectancy_not_world)
sumOfAllX = numpy.nansum([pow(i - life_expectancy_world_sum, 2) for i in list_life_expectancy_not_world])
print(sumOfAllX)

sigmasquared = sumOfAllX / n
print(sigmasquared)
sigma = pow(sigmasquared, 0.5)
print("Life expectancy in the world is", life_expectancy_world_sum, "and the standard deviation is", sigma,
      "and the GDP is", gdp_world_sum)
data_above_standard_deviation = data_not_world[data_not_world['Life expectancy'] > life_expectancy_world_sum + sigma]
countries_above_standard_deviation = data_above_standard_deviation['Entity']
print("Number of countries with life expectancy above the standard deviation: ",
      countries_above_standard_deviation.size)
print("Countries with life expectancy above the standard deviation:\n", countries_above_standard_deviation)

higher_life_expectancy = data_not_world[data_not_world['Life expectancy'] > life_expectancy_world_sum]
lower_gdp_higher_life_expectancy = higher_life_expectancy[higher_life_expectancy['GDP per capita'] < gdp_world_sum]
print("Size of number of countries with low gdp but higher life expectancy",
      lower_gdp_higher_life_expectancy['Entity'].size)
print("Countries with higher life expectancy and lower GDP:\n", lower_gdp_higher_life_expectancy['Entity'])

higher_gdp_than_world = data_not_world[data_not_world['GDP per capita'] > gdp_world_sum]
print("Number of countries with higher GDP than the world", higher_gdp_than_world['Entity'].size)
lower_gdp_than_world = data_not_world[data_not_world['GDP per capita'] < gdp_world_sum]
print("Number of countries with lower GDP than the world", lower_gdp_than_world['Entity'].size)
higher_gdp_and_lower_life_expectancy = higher_gdp_than_world[
    higher_gdp_than_world['Life expectancy'] < life_expectancy_world_sum]
print("Size of number of countries with higher gdp but lower life expectancy",
      higher_gdp_and_lower_life_expectancy['Entity'].size)
print("Countries with higher GDP and lower life expectancy:\n", higher_gdp_and_lower_life_expectancy['Entity'])

dt = pd.read_csv("/Users/jonathannaumanen/Downloads/Happiness-WVS-vs-Gallup.csv")
data_happiness_14 = dt[dt['Year'] == 2014]
lower_than_70_percent_happiness = data_happiness_14[data_happiness_14['Share of people who are happy (World Value Survey 2014)'] < 70]
print("Number of countries with happiness lower than 70%: ", lower_than_70_percent_happiness['Entity'].size)
print("Countries with happiness lower than 70%:\n", lower_than_70_percent_happiness['Entity'])
data_happiness_14_not_egypt = data_happiness_14[data_happiness_14['Entity'] != 'Egypt']
xValues_happiness = data_happiness_14_not_egypt['Share of people who are happy (World Value Survey 2014)']
yValues_life_satisfaction = data_happiness_14_not_egypt['Life satisfaction in Cantril Ladder (World Happiness Report 2022)']
sad_country = data_happiness_14[data_happiness_14['Share of people who are happy (World Value Survey 2014)'] < 40]
print("Saddest country :( ", sad_country['Entity'])
low_life_satisfaction = data_happiness_14[data_happiness_14['Life satisfaction in Cantril Ladder (World Happiness Report 2022)'] < 5]
low_life_satisfaction_but_happy = low_life_satisfaction[low_life_satisfaction['Share of people who are happy (World Value Survey 2014)'] > 90]
print("Countries with low life satisfaction but happy people:\n", low_life_satisfaction_but_happy['Entity'])
plt.xlabel('Share of people who are happy')
plt.ylabel('Life satisfaction')
plt.scatter(xValues_happiness, yValues_life_satisfaction, edgecolors='black', linewidths=0.5, s=25)
plt.show()