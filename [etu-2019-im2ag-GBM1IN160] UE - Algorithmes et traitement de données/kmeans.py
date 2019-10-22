#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.decomposition import PCA

# Fetch dataset from sklearn and initialize dataset-dependent variables to be used in kmeans
dataset = load_iris()
x = dataset.data # Samples represented in feature space
y = dataset.target # Ground-truth class for each sample
n_samples = x.shape[0] # Number of samples in the dataset
n_features = x.shape[1] # Dimension of samples' feature space
n_classes = len(set(y)) # Number of ground-truth classes (i.e., number of unique values in y)

# Hyperparameters
n_clusters = 4 # Number of clusters to consider (e.g., equal to the number of ground-truth classes)
n_runs = 1 # Number of time k-means will be run, and from which average performance will be computed

average_nmi = 0

for run in range(0, n_runs):
    # Initialize cluster centroids
    # indices = np.random.randint(n_samples, size = n_clusters) # Draw n_clusters samples without replacement
    indices = np.random.choice(n_samples, size = n_clusters, replace=False) # Draw n_clusters samples without replacement
    c = [x[i] for i in indices] # Use these n_clusters samples to initialize the centroids

    # K-Means algorithm
    diff = 1 # Number of assignments changed between successive iterations
    assignments = np.zeros(n_samples) # Cluster assignment for each sample
    while diff > 0:
        # Assign samples to clusters, based on nearest cluster centroid
        assignments_old = np.array(assignments) # Save old assignments to compute diff
        for i in range(0, n_samples):
            nearest_centroid = 0 # Index of the centroid which is the nearest from current sample x[i]
            min = float("inf") # Distance between current sample x[i, :] and nearest centroid
            for j in range(0, n_clusters):
                dist = np.linalg.norm(x[i] - c[j]) # Distance between sample x[i] and centroid c[j]
                if dist < min:
                    min = dist
                    nearest_centroid = j
            assignments[i] = nearest_centroid
        diff = sum(assignments - assignments_old) # Is 0 iff successive assignments are unchanged

        # Update centroids
        for j in range(0, n_clusters):
            x_assigned_j = [x[i] for i, assignment in enumerate(assignments) if assignment == j] # Samples assigned to cluster j
            if len(x_assigned_j):
                c[j] = 1.0/len(x_assigned_j)*sum(x_assigned_j) # Cluster centroid is updated as the average of its assigned samples
            else:
                # Otherwise don't update it
                print("Cluster vide, centroïde inchangé.")
    #print(assignments) # Print the cluster assignments for all samples

    # Evaluate the obtained clustering based on the ground-truth classes
    nmi = normalized_mutual_info_score(assignments, y)
    print("NMI pour l'exécution {}: {:.2f}".format(run, nmi))
    average_nmi = average_nmi + nmi

    # Compare the obtained clustering and ground-truth classes by visualizing data in 2D space using PCA
    pca = PCA(n_components=2)
    x_r = pca.fit(x).transform(x) # x after dimension reduction based on a 2-component PCA

    # Visualization for ground-truth classes
    colors = ['navy', 'turquoise', 'darkorange']
    target_names = dataset.target_names # Labels for iris species
    plt.figure()
    for color, i, target_name in zip(colors, [0, 1, 2], target_names):
        plt.scatter(x_r[y == i, 0], x_r[y == i, 1], color=color, label=target_name)
    plt.legend(loc='best')
    plt.title('Partition réelle sur la collection Iris')

    # Visualization for the clustering obtained by k-means
    k = len(set(assignments))
    print(k)
    target_names = range(k) # Obtained cluster labels
    plt.figure()
    for i, target_name in zip(range(k), target_names):
        plt.scatter(x_r[assignments == i, 0], x_r[assignments == i, 1],
                    label=target_name)
    plt.legend(loc='best')
    plt.title('Partition obtenue par k-means sur la collection Iris')

    plt.show()

print("NMI moyenne: {:.2f}".format(average_nmi/n_runs))