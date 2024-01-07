import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("aaii_data.xls")
df.dropna(inplace=True)
df2 = df.iloc[:1906]

# Set the second row as column names
df2.columns = df2.iloc[0]

# Drop the second row from the DataFrame using the index
df2 = df2.drop(df2.index[0])

# Reset the index
df2 = df2.reset_index(drop=True)
plt.plot(df2['Spread'])
plt.show()
