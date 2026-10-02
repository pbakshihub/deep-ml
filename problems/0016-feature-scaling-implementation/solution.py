import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	eps = 1e-8
	mean = np.mean(data,axis=0)
	std = np.std(data,axis=0)
	data_std = (data - mean)/(std + eps)
    
	data_min = np.min(data,axis=0)
	data_max = np.max(data,axis=0)
	data_norm = (data - data_min)/((data_max - data_min)+eps)

	return np.round(data_std,4), np.round(data_norm,4)