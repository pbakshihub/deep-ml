import numpy as np
def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here

    x = np.array(x)
    x_min = np.min(x,axis=0)
    x_max = np.max(x,axis=0)
    x_minmax = [(i - x_min)/(x_max - x_min) for i in x]
    return x_minmax
    pass