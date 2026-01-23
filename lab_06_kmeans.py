# import necessary libraries
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# creating synthetic dataset for clustering
# manual data as per instructions
x_data = np.array([[2, 55], [3, 60], [4, 65], [5, 70],
                   [6, 75], [7, 80], [8, 85], [9, 90], [10, 95]])

print("Feature Data:\n", x_data)

# visualizing initial data
plt.scatter(x_data[:, 0], x_data[:, 1])
plt.xlabel('Study hours per week')
plt.ylabel('Attendance rate (%)')
plt.title("Student Study Hours vs Attendance Rate")

# performing k-means clustering
# using k=3
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(x_data)
labels = kmeans.labels_

# visualizing the clusters
plt.scatter(x_data[:, 0], x_data[:, 1], c=labels, cmap='viridis')
# plotting centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            c='red', marker='o', s=100, label='Centroids')
plt.xlabel('Study hours per week')
plt.ylabel('Attendance rate (%)')
plt.title("K-Means Clustering of Students")
plt.legend()

# choosing optimal k using elbow method
inertia_list = []
k_range = range(1, 10)

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(x_data)
    inertia_list.append(km.inertia_)

plt.plot(k_range, inertia_list, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title("Elbow Method for Optimal k")
plt.show()