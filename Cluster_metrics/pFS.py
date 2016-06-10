import numpy as np

def pfs_(labels,X, cluster_centre=None):

	"""
	Calculate pFS value for a given clustering results
	------
	Input:
		labels:
			numpy array with cluster labels
		X:
			numpy array (shape = (data point count,
			dimensions)
			data points used in the clustering
		cluster_centre:
			numpy array (shape = (dimensions,
			unique labels))
			array with coordinates of each centroid
			and assumed to correspond labels in ascending
			fashion.
			Default is None, so if not provided the average
			will be calculated
	"""
    
    # initiate numpy array
    sse = np.zeros(np.unique(labels).size)
    
    # between-cluster-sum-of-squares
    for i, label in enumerate(np.unique(labels)):
    	if cluster_centre = None:
    		cluster_centre_i = X[labels == label].mean(0)
    	else:
    		cluster_centre_i = cluster_centre[i]
        sse[i] = ((X[labels == label] - cluster_centre_i)**2).sum()
    
    # sum of all between-cluster-sum-of-squares (for all k)  
    sse = sse.sum()
    
    # within-cluster-sum-of-squares of all clusters
    sst= ((X - X.mean(0))**2).sum()
    
    # r squared value
    r_2 = (sst - sse)/sst
    
    # pFS, r^2
    return (r_2 / (np.unique(labels).size - 1)) / ((1 - r_2) / 
    		(X.shape[0] - np.unique(labels).size)), r_2