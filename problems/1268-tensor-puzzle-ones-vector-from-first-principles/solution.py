import numpy as np

def ones(n: int) -> np.ndarray:
    """Return a length-n float vector of ones without calling np.ones."""
    # Your code here
    one = [i/i for i in range(1,n+1)]
    return one

    pass
