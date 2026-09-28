import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    # Your code here
    n = A.shape[0]
    indices = np.arange(n)
    return A[indices,indices]
    pass
