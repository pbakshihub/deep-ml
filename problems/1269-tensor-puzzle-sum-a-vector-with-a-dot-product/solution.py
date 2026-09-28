import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    # Your code here
    n = len(a)
    one = [i/i for i in range(1,n+1)]
    total = np.dot(a,one)
    return total
    pass
