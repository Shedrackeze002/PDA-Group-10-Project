# Intentional Homicide: Exploratory Data Analysis (Group 10)




Metadata: Course: Programming for Data Analytics (04-638); Instructor: [Instructor]; Assignment: EDA and Reporting; Group members: Group 10; Submission date:




## Abstract

This report presents exploratory analysis of the UNODC "Intentional Homicide Victims" dataset. We describe data preparation, summarize key statistics, and highlight major patterns in counts and rates of homicide across countries and regions. Using UN population estimates from the World Bank, we compute homicide rates per 100,000 population to allow fair comparisons. The analysis focuses on eight guiding questions addressing country-level extremes, global trends, regional differences, concentration among top countries, mechanisms, sex and age patterns, and distributional outliers.




## Background and Problem Description

Homicide is a critical public health and criminal justice indicator. The UNODC dataset provides counts of intentional homicide victims by country and year with disaggregation by sex, age, and other dimensions where available. Our goal is to produce reproducible EDA that answers a subset of preliminary questions and offers insights for policy and further analysis.




## Methods

We loaded the cleaned counts produced from the UNODC Excel data. Population series were fetched from the World Bank API and merged on ISO3 country codes and year to compute homicide rates per 100,000 population. We selected observations labelled as totals (Category/Sex/Age marked "Total" where available) and aggregated counts by country-year before computing rates. Visualizations include bar charts, time series, histograms, and boxplots to reveal distributions and outliers. The notebook contains the code and the outputs directory stores plots and CSVs.




## Results and Discussion

1) Country extremes (rates, 2023): The highest homicide rates (per 100k) in 2023 were observed in: 

- Jamaica: 51.04 per 100k

- Ecuador: 45.98 per 100k

- Haiti: 41.51 per 100k

- Honduras: 31.74 per 100k

- Mexico: 24.88 per 100k

- Costa Rica: 18.09 per 100k

- Bermuda: 15.74 per 100k

- Puerto Rico: 14.99 per 100k

- Mongolia: 6.00 per 100k

- United States of America: 5.88 per 100k




The countries with the lowest non-zero rates in the same year include:

- Oman: 0.14 per 100k

- Singapore: 0.19 per 100k

- Slovenia: 0.59 per 100k

- Switzerland: 0.60 per 100k

- Malta: 0.64 per 100k




2) Global trend: Aggregating counts across countries shows temporal variation; see the global trend figure. The counts series is dominated by a small set of countries with large absolute values, making rates essential for fair comparison.




3) Regional comparison: In the most recent year, the highest total counts are concentrated in the following regions (by descending counts):

- Americas: 428,394 counts

- Asia: 18,815 counts

- Europe: 17,065 counts

- Africa: 8,424 counts

- Oceania: 923 counts




4) Concentration: The top 10 countries by counts in 2023 account for approximately 95.2% of global counts in that year, indicating moderate-to-high concentration of homicides among a limited group of countries.




5) Mechanisms: The dataset includes a dimension indicating category/source; aggregated distribution by that field is available in `mechanism_distribution.csv` and plotted in the notebook. Interpret with caution as coding varies by country.




6) Sex differences: In the most recent year, male victims account for the majority of recorded homicide counts; see the sex distribution figure for exact shares.




7) Age groups: Aggregated totals by age show which age group carries the largest share of victims; results are presented in the notebook and saved outputs.




8) Distribution and outliers: The counts distribution is highly skewed with long right tail; boxplots and histograms reveal outliers—primarily large counts from populous or high-violence countries. We report both counts and rates to mitigate population-driven distortions.




## Conclusion

This EDA highlights that (a) high absolute counts are concentrated in a small subset of countries, (b) rates per 100k provide a different ranking and are essential for fair comparison, and (c) sex and age patterns mirror broader criminal victimization patterns. The notebook and outputs include reproducible code, plots, and CSVs to support these findings.




## References

- UNODC Data Portal: Intentional Homicide Victims series

- World Bank population indicators (SP.POP.TOTL)


