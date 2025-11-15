import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def weatherCondition(a):
    if a <= 1 and a > 0:
        return("Very Light")
    elif a > 1 and a <= 5:
        return("Light")
    elif a > 5 and a <= 20:
        return("Moderate")
    elif a > 20 and a <= 50:
        return("Heavy")
    elif a > 50 and a <= 75:
        return("Very Heavy")
    elif a > 75 and a <= 100:
        return("Severe")
    elif a == 0:
        return("No Rain")
    
def dayCondition(df_2):
    x = df_2["precipitation_sum (mm)"]
    y = df_2["snowfall_sum (cm)"]
    if x == 0 and y == 0 :
        return("Dry")
    elif x - y == 0:
        return("Snowy")
    elif x - y > 0 and y != 0:
        return("Mixed")
    else:
        return("Rainy")
df = pd.read_csv("munich.csv" , sep=";", encoding="utf-8")
df_1 = df.copy()
df["precipitation_sum (mm)"] = df["precipitation_sum (mm)"].fillna("0").astype(float)
df["snowfall_sum (cm)"] = df["snowfall_sum (cm)"].fillna("0").astype(float)
#temizledih veriyi
df_1.dropna(how="any", inplace=True)
df_2 = df_1.copy()
df_1["precipitation_sum (mm)"] = df_1["precipitation_sum (mm)"].apply(weatherCondition)
weat_cond = df_1["precipitation_sum (mm)"].value_counts()
day_cond = df_2.apply(dayCondition, axis=1)
day_cond = day_cond.value_counts()
#visualation
plt.bar(weat_cond.index,weat_cond.values)
plt.xlabel("Precipitation Type")
plt.ylabel("Count")
plt.show()
plt.bar(day_cond.index,day_cond.values)
plt.xlabel("Day Condition")
plt.ylabel("Count")
plt.show()