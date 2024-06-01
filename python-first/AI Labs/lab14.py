import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = load_iris()
X = iris.data

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize KMeans with 3 clusters (since we have 3 species of iris)
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit the KMeans model to the scaled data
kmeans.fit(X_scaled)

# Get the cluster labels
cluster_labels = kmeans.labels_

# Visualize the clustering results
plt.figure(figsize=(8, 6))

# Scatter plot for sepal length vs sepal width
plt.subplot(2, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Sepal Width')

# Scatter plot for petal length vs petal width
plt.subplot(2, 2, 2)
plt.scatter(X[:, 2], X[:, 3], c=cluster_labels, cmap='viridis')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Petal Length vs Petal Width')

# Plot cluster centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=100, color='red', label='Centroids')
plt.legend()

plt.tight_layout()
plt.show()
