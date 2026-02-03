import matplotlib.pyplot as plt
import pandas as pd
import random as r

countries = pd.read_csv('CountriesSD.csv')
summer = pd.read_csv('SummerSD.csv')
winter = pd.read_csv('WinterSD.csv')

r.seed()
plt.subplot(1,1,1)
plt.bar(winter['Medal'].head(15),winter['Athlete'].head(15))
plt.show()
