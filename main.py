# This is a sample Python script.
import numpy
from numpy import nan
# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import matplotlib.pyplot as plt

from math import sqrt

df = pd.read_csv("/Users/jonathannaumanen/Downloads/life-expectancy-vs-gdp-per-capita.csv")

data_18 = df[df['Year'] == 2018]
data_pop = data_18[data_18['Population (historical estimates)'] > 1000000]
# print(data_18)

yValues = data_pop['Life expectancy']
xValues = data_pop['GDP per capita']

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

dt = pd.read_csv("/Users/jonathannaumanen/Downloads/interpersonal-trust-vs-income-inequality.csv")
data_trust_18 = dt[dt['Year'] == 2014]
data_trust_pop = data_trust_18[data_trust_18['Population (historical estimates)'] > 1000000]
data_trust_world = data_trust_pop[data_trust_pop['Entity'] == 'World']
trust_world = data_trust_world['Trust in others (World Values Survey (2014))']
trust_world_sum = trust_world.sum()
print("Trust in the world is", trust_world_sum)