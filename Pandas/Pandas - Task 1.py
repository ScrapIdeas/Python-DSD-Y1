import pandas as pd
import time
df = pd.read_csv('students.csv')
# atrisk = pd.DataFrame("A")
above_80 = df[df['Attendance'] >= 90 ]
# atrisk = pd.concat(above_80)
df.head()
# atrisk.head()
print(df['Name'].count())
# print(above_80)
# time.sleep(25)
print(df)
df.info()