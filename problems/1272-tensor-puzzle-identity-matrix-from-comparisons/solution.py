import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    # Your code here
    # Create a 1-D coordinate array [0, 1, ..., n-1]
    indices = np.arange(n)
    
    # Broadcast a column vector (n, 1) against a row vector (1, n)
    # The comparison evaluates to True where row index equals column index
    boolean_identity = indices[:, None] == indices[None, :]
    
    # Cast the boolean array to a float64 array (True -> 1.0, False -> 0.0)
    return boolean_identity.astype(np.float64)
    pass
