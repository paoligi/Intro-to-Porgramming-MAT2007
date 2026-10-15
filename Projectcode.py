#Import packages
import numpy as np
import pandas as pd
import pycountry_convert as cc
import matplotlib.pyplot as plt
from scipy import stats


#Import dataset
data = pd.read_csv("2019.csv")

#Check quality checks
def quality_checks():
    print("\n=== Quality Checks Dataset ===")
    print(data.head())              #Check if reading works
    data.info()                     #Checks whether how many non-null inputs there are and the datatype per column
    print(data.isnull().sum())      #Checks whether there are any invalid inputs
    print(data.duplicated().sum())  #Checks whether there are any duplicate rows
    print(data.describe())          #Finds information such as mean, count, std, min, max for each column -> helps determine outliers


#Cleaning names for country_convert and Getting continent information
def get_continent(country):
    if country == "Trinidad & Tobago":
        country = "Trinidad and Tobago"

    if country == "Congo (Brazzaville)":
        country = "Congo"

    if country == "Congo (Kinshasa)":
        country = "Congo, The Democratic Republic of the"

    if country == "Kosovo":
        return "EU"

    if country == "Palestinian Territories":
        return "AS"
    country_code = cc.country_name_to_country_alpha2(country)
    continent_code = cc.country_alpha2_to_continent_code(country_code)
    return continent_code

#Add a column with continent association
data["Continent"] = data["Country or region"].apply(get_continent)

#Quality check of additional continent column
def check_continent():
    print("\n=== Quality Checks Continent Data ===")
    print(data[["Country or region", "Continent"]])
    print(data["Continent"].isnull().sum())
    print(data["Continent"].value_counts())


#Research Question Part 1: Regional differences in Happiness scores
def Continent_differences():
    #Calculate regional means and standard deviation
    Continent_means = data.groupby("Continent")["Score"].mean()
    Continent_std = data.groupby("Continent")["Score"].std()

    #Plot regional means and standard deviation
    Continent_means.plot(kind = "bar", yerr = Continent_std.values, capsize=5, color=["tab:blue", "tab:orange", "tab:green",
           "tab:red", "tab:purple", "tab:brown"])
    
    plt.xlabel("Continents")
    plt.ylabel("Mean happiness score")
    plt.ylim(0,10)
    plt.title("Mean Happiness Score by Continent (±1 SD)")
    plt.grid(alpha=0.2)
    
    plt.savefig("Continent differences")
    plt.show()

    #Print the highest and lowest average Happiness Scores with associated continent.
    print("\n=== Part 1: Happiness Scores ===")
    print("Highest mean:", round(Continent_means.max(), 3),"- Continent:", Continent_means.idxmax())
    print("Lowest mean:", round(Continent_means.min(), 3), "- Continent:", Continent_means.idxmin())

    #Welch's ANOVA test: statistical test, where data does violates assumption that variances need to be equal
    #Exclude Oceania because it only contains 2 countries
    ANOVA_data = data[data["Continent"] != "OC"]

    Scores_by_continent = []
    for continent, group in ANOVA_data.groupby("Continent"):
        Scores_by_continent.append(group["Score"].values)

    F, p = stats.f_oneway(*Scores_by_continent, equal_var=False)

    print("p-value:", p)

    if p<0.05:
        print("The difference between continent means is statistically significant.")
    else:
        print("The difference between continent means is not statistically significant.")


#Research Question Part 2: Modeled Factor Contributions per continent
def Factor_contribution():
    #Select six factors
    Factors = ["GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]

    #Calculate the mean for each of the six factors for each continent
    Continent_factor_means = data.groupby("Continent")[Factors].mean()

    #Create second graph
    Continent_factor_means.plot(kind="bar", figsize=(12,7))

    plt.xlabel("Continents")
    plt.ylabel("Modelled Contribution to Happiness Score")
    plt.title("Factor Contributions to Happiness Scores by Continent")
    plt.grid(alpha=0.2)

    plt.savefig("Factor contributions")
    plt.show()

    #Print mean contribution of largest contributing factor for each continent
    print("\n=== Part 2: Factor Contributions ===")
    Results = pd.DataFrame({
    "Largest factor": Continent_factor_means.idxmax(axis=1),
    "Mean contribution": Continent_factor_means.max(axis=1)})

    print(Results)


#Run the sections:
quality_checks()
check_continent()
Continent_differences()
Factor_contribution()

