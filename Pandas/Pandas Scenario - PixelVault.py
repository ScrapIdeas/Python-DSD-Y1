import pandas as pd
df = pd.read_csv('pixelvault.csv')
df1 = df.drop_duplicates(subset=None,keep='first',inplace=False)
df.update(df1)

dfgameslist = df['game_title']
AppearsMost = dfgameslist.mode(dropna=True)

total_sale = df['total_sale'].max()

Highest = df.iloc[df['quantity'].max()]

averagegames = df['price'].()

print(df)
print(AppearsMost)
print(Highest)
print(total_sale)
print(int(averagegames))

#P.S. You're welcome for the link, got around to doing it. :o)