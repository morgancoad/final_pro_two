# Does Public Transportation impact crime rates

There are plenty of benefits for state and federal governments to provide the option of public transportation to communities. Some of those benefits include but are not limited to financial, creating jobs, reducing air pollution, and reducing traffic congestion. But are there negative impacts of public transportation? In this analysis we will take a look at whether counties with public transportation have higher crime rats than counties without public transportation.

## Table of Contents 
1. Data
2. Methodology and Null/Alternate Hypothesis
3. Average Crime Rate 2016-2020
4. Public Transportation 2016-2020
5. Results of Hypothesis Test
6. Opportunities for Exploration

# Data

## Crime Data

The Division of Criminal Justice Services collects and compiles reports from more than 500 New York State police and sheriff’s departments. These statistics are submitted to the FBI under the National Uniform Crime Reporting (UCR) Program. Data available from 1990-2021. This data can be found at the following hyperlink, [Crime_Data](https://data.ny.gov/Public-Safety/Index-Crimes-by-County-and-Agency-Beginning-1990/ca8h-8gjq)

## Public Transportation Data

The National Transit Database collects and compiles reports from most public transportation agencies in the US. These reports are submitted to the Federal Transit Authority and are subjected to analysis and validation. The data used in this analysis is from 2016-2020. This data can be found at the following hyperlink, [Transportation](https://www.transit.dot.gov/ntd/ntd-data)

## Population Data

The New York State Department of Labor provides resident population of New York State and counties based on census counts. Data available from 1970-2021. This data can be found at the following hyperlink, [Population](https://data.ny.gov/Government-Finance/Annual-Population-Estimates-for-New-York-State-and/krt9-ym2k)

# Methodology and Null/Alternate Hypothesis

Null Hypothesis: Average crime rate in counties with public transportationare equal to or less than the crime rate in counties without public transportataion.

Alternate Hypothesis: Average crime rate in counties with public trans are higher than the crime rate in counties without public transportation.

<p align="center">
<img src="images\methodology.png" width = 600>
</p>

# Average Crime Rate 2016-2020

<p align="center">
<img src="images\full_crime_rate_choropleth.png" width = 600>
</p>

The counties with higher crime rates are inidcated by lighter colors. The categories included in crime rate are murder, rape, robbery, aggravated assault, burglary, larceny, vandalism, and motor vehicle theft.

# Public Transportation 2016-2020

<p align="center">
<img src="images\public_trans_discrete.png" width = 600>
</p>

There are 14 counties with public transportation and 48 counties without public transportation.

<p align="center">
<img src="images\public_trans_continuous.png" width = 600>
</p>

The counties with the most passenger miles traveled are indicated by lighter colors. However, the amount of passenger miles traveled in New York city are drastically higher, dulling other areas with public transportaion.

# Results of Hypothesis Test

With an alpha of .05 I failed to jeject the null hypothesis. As you can see below the average crime rates per year from both, areas with public transportation and areas without public transportation are close in proximity, indicating that the difference in crime rate isnt significant enough to reject the null hypothesis. The p-value calculated for the test was.63 

<p align="center">
<img src="images\hypothesis_results.png" width = 600>
</p>

# Opportunities for Exploration

For the time period 2016-2020 aggregated I did a quick correlation of the subcategories and came up with the below results. Deeper analysis would need to be done to one-hot encode the counties so a proper correlation calculation could be done. 

<p align="center">
<img src="images\crime_correlation.png" width = 600>
</p>
