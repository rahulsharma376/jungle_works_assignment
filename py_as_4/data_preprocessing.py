import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


df = pd.read_csv('Mall_Customers.csv')

#Normalizing the similar datatypes
# print(df.info())
feature = df[['CustomerID', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

scal = StandardScaler()
similar_feature = scal.fit_transform(feature)

# sns.pairplot(df[['CustomerID', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']])
# plt.show()

# df[['CustomerID', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']].hist()
feature.hist()
plt.show()

wcss = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters=i, random_state = 42)
#     kmeans.fit(similar_feature)
#     wcss.append(kmeans.inertia_)

# plt.plot(range(1, 11), wcss)
# plt.xlabel('Number of Clusters')
# plt.ylabel('WCSS')
# plt.show()


kmeans = KMeans(n_clusters = 6, random_state = 42)
cust_label = kmeans.fit_predict(similar_feature)

feature['Cluster'] = cust_label

pca = PCA(n_components=2)
data_pca = pca.fit_transform(similar_feature)

plt.scatter(data_pca[:, 0], data_pca[:, 1], c = cust_label, cmap='Viridis')
plt.title('Customer Segments')
plt.show()

