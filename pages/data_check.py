import pandas as pd
import numpy as np


available_cols = [
	'iso_code', 
	'continent', 
	'location', 
	'date', 
	'total_cases', 
	'new_cases', 
	'total_deaths', 
	'new_deaths', 
	'total_cases_per_million',
	'new_cases_per_million', 
	'total_deaths_per_million', 
	'new_deaths_per_million', 
	'total_tests', 
	'new_tests', 
	'total_tests_per_thousand', 
	'new_tests_per_thousand', 
	'new_tests_smoothed', 
	'new_tests_smoothed_per_thousand', 
	'tests_units', 
	'stringency_index', 
	'population', 
	'population_density', 
	'median_age', 
	'aged_65_older', 
	'aged_70_older', 
	'gdp_per_capita', 
	'extreme_poverty', 
	'cvd_death_rate', 
	'diabetes_prevalence', 
	'female_smokers', 
	'male_smokers', 
	'handwashing_facilities', 
	'hospital_beds_per_thousand'
]

cols = [
	'iso_code',
	'continent',
	'location',
	'date',
	'total_cases',
	'new_cases',
	'total_deaths',
	'new_deaths'
]



df = pd.read_csv('data/owid-covid-data.csv', usecols=cols)
# .dropna()
# df_nan = df.dropna()

df_global_cases = df.loc[df.location == 'World']

# print(df_global_cases, df_global_cases['date'])

# print(df, [x for x in df.columns])

