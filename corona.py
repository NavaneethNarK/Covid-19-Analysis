# import all the required python modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# read the file corona.csv
corona_dataset_csv=pd.read_csv("corona.csv")

# remove the column "Lat" and "Long"
df = corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)

# Group all the provinses according to the country
corona_dataset_aggrigated=corona_dataset_csv.groupby("Country/Region").sum()

# add a new column called max_infected rate 
countries=list(corona_dataset_aggrigated.index)
max_infection_rate=[]
for c in countries:
    max_infection_rate.append(corona_dataset_aggrigated.loc[c].diff().max())
corona_dataset_aggrigated["max_infection_rate"]=max_infection_rate

# take only the country name and the max_infected_rate
corona_data=pd.DataFrame(corona_dataset_aggrigated["max_infection_rate"])

# read from the file hapiness.csv 
happiness_report_csv=pd.read_csv("happiness.csv")

# remove all the unwanted columns 
useless_cols = ["Overall rank","Score","Generosity","Perceptions of corruption"]
happiness_report_csv.drop(useless_cols,axis=1,inplace=True)
happiness_report_csv.set_index("Country or region",inplace=True)

# join the corona data and happiness data
data = corona_data.join(happiness_report_csv,how="inner")

# plot the graph showing the relation between per capita and infection rate
x=data["GDP per capita"]
y=data["max_infection_rate"]
sns.regplot(x,np.log(y))
plt.show()
