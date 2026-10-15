# Happiness Report Analysis
This project explores the differences in average Happiness Scores and average modeled factor contributions across continents, using the 2019 Happines Report dataset.

## Research Question
Do average Happiness Scores differ across continents and are there differences in the factors contributing to these scores?

## Dataset
Dataset: Sustainable Development Solutions Network (2019). *World Happiness Report*. 

Source: https://www.kaggle.com/datasets/unsdsn/world-happiness

File: 2019.csv

The dataset contains data on the Happiness Scores of 156 countries, which originate from the Gallup World Poll. Additionally, for each country, the dataset contains data on the modeled contribution of GDP per capita, social support, healthy life expectancy, freedom to make life choices, generosity, and perceptions of corruption to the Happiness Score. 

Before the analysis, quality checks were conducted to look for missing values or duplicates.
No missing values or duplicates were found. To group country data into continents, the pycountry-convert python package was used.

## What the Script Does
The Python script `Projectcode.py´
- Imports the 2019.csv
- Conducts quality checks

For first part of research question:
- Cleans certain country names for adherance to pycountry-convert norm
- Adds continent information to each country 
- Checks quality of new continent column
- Calculates average happiness scores and standard deviation per continent and visualizes it
- Prints highest and lowest average happiness scores and the associated continents.
- Conducts a Welch's ANOVA test, while excluding Oceania (due to limited data for it).

For second half of research question:
- Calculates average modeled contribution per factor for each continent, and visualizes it.
- Prints the largest contributing factor with its mean contribution for each continent.

## Output
The script generates:
- 'Continent differences.png'
- 'Factor contributions.png'

## Dependencies
The analysis requires Python and the following packages:
- numpy 
- pandas
- pycountry_convert
- matplotlib
- scipy

Install the required packages with:
- pip install numpy
- pip install pandas
- pip install pycountry_convert
- pip install matplotlib
- pip install scipy

## How to run
```bash
py Projectcode.py
``` 


