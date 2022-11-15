import numpy as np 

def EuilidDistance(datapoint, centroid):
    return np.sqrt(np.sum((datapoint - centroid)**2))

def assignLabel(distance):
    return min(distance, key=distance.get)

def KMeans(datapoints, centroids, totalIters):
    label = []
    clusterlabel = []
    
    for i in range(totalIters):
        for datapoint in datapoints:
            distance = {}
            for index in range(len(centroids)):
                distance[index] = EuilidDistance(datapoint, centroids[index])
            
            label = assignLabel(distance)
            centroids[label] = np.array(centroids[label] + datapoint)/2
            
            if i == totalIters - 1:
                clusterlabel.append([datapoint, label])
    return clusterlabel, centroids
    
centroids = np.array([[50.0, 0.0], [45.0, 70.0], [30.0, 92.0]])
datapoints =  np.array([[15, 16],
               [16, 18.5],
               [17, 20.2],
               [16.4, 17.12],
               [17.23, 18.12],
               [43, 43],
               [44.43, 45.212],
               [45.8, 54.23],
               [46.313, 43.123],
               [50.21, 46.3],
               [99, 99.22],
               [100.32, 98.123],
               [100.32, 97.423],
               [102, 93.23],
               [102.23, 94.23]])

clusterlabel, newCentroids = KMeans(datapoints, centroids, 100)
print("The result is: ")
for label in clusterlabel:
    print(f"datapoint: {label[0]}")
    print(f"Cluster: {label[1]}")
    print()

print("Centroids: ")
print(newCentroids)
            
            
            