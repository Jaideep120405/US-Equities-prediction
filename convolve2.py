import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")
print(df.head())
X = df.drop(['Unnamed: 0','y'],axis=1)
y = df['y']
correlation_matrix = X.corr()

# # Plotting the correlation matrix using Seaborn
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlation_matrix, cmap='coolwarm', fmt=".2f", linewidths=.5)
# plt.title('Correlation Matrix')
# plt.show()

# # Flatten the upper triangle of the correlation matrix (excluding the diagonal)
# upper_triangle = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool))

# # Find the least 20 correlated column pairs
# least_correlated_pairs = upper_triangle.unstack().sort_values().head(20)

# # Extract the column names from the indices
# least_correlated_columns = least_correlated_pairs.index.tolist()

# # Print the least correlated pairs
# print("Least Correlated Pairs:")
# print(least_correlated_pairs)



# Scale the features to the range [0, 1] using MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Use SelectKBest with chi-squared test to select top 20 features
k_best = 20
selector = SelectKBest(chi2, k=k_best)
X_train_selected = selector.fit_transform(X_train, y_train)

# Get the indices of the selected features
selected_indices = selector.get_support(indices=True)

# Print the indices of the selected features
print("Selected Feature Indices:", selected_indices)


Variables = X.columns
Mark = [0]*40
for i in selected_indices:
    Mark[i] = 1

data = {"Variables":Variables,"Mark":Mark}
df3 = pd.DataFrame(data)

df3.to_csv('output.csv',index = False)