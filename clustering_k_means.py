# import necessary libraries
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
# creating synthetic dataset for clustering
x_data = np.array([[2, 55], [3, 60], [4, 65], [5, 70],
                  [6, 75], [7, 80], [8, 85], [9, 90], [10, 95]])
print("Feature Data:\n", x_data)
plt.scatter(x_data[:, 0], x_data[:, 1])
plt.xlabel('Study hours per week')
plt.ylabel('Attendance rate (%)')
plt.title("Student Study Hours vs Attendance Rate")

#  performing k-means clustering 

Kmeans = KMeans(n_clusters=3, random_state=42)
Kmeans.fit(x_data)
labels = Kmeans.labels_
plt.scatter(x_data[:, 0], x_data[:, 1], c=labels, cmap='viridis')
plt.scatter(Kmeans.cluster_centers_[:, 0], Kmeans.cluster_centers_[
            :, 1], c='red', marker='o', s=100, label='Centroids')
plt.xlabel('Study hours per week')
plt.ylabel('Attendance rate (%)')
plt.title("K-Means Clustering of Students")
plt.legend()

# choosing optimal k using elbow method

inertia = []
k_range = range(1, 10)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(x_data)
    inertia.append(km.inertia_)
plt.plot(k_range, inertia, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title("Elbow Method for Optimal k")
plt.show()