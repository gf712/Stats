import numpy as np
from itertools import permutations

def dbi_(labels, X, cluster_centre):
    
    permutation = permutations(np.unique(labels),2)

    # calculate all inter distances
    s = np.zeros((np.unique(labels).size))
    for label in np.unique(labels):

        s[label] = np.sqrt(((X[labels==label] - cluster_centre[label]) ** 2).sum(1)).mean()
    
    # initiate variables
    pair_i = None
    d = []
    r_ij= []
    
    # calculate the dbi for each permutation and group them up by cluster label 
    for pair in permutation:
                 
        m_i = np.sqrt(((cluster_centre[pair[0]] - cluster_centre[pair[1]])**2).sum(0))

        r_i = (s[pair[0]] + s[pair[1]]) / m_i
        
        
        # group up permutations (i.e. (1,2) and (1,3), but not (1,2) and (2,1))
        if pair[0] == pair_i or pair_i == None:
            r_ij.append(r_i)         
        
        # get max r_i from db and reinitialize variable for new group of permutations
        # This is, the worst case scenario and is used in the original definition of DBI
        # https://en.wikipedia.org/wiki/Davies–Bouldin_index
        # can change definition here, e.g. (weighted) average d
        else:            
            d.append(max(r_ij)) 
            
            # new group
            r_ij = []
            r_ij.append(r_i)
        
        # update cluster ID that was processed
        pair_i = pair[0]
    
    # calculate DBI from db
    
    return sum(d) / len(d) 