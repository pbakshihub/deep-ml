import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    indices = list(range(n_samples))
    if shuffle:
        np.random.shuffle(indices)

    # First (n_samples % k) folds get one extra sample
    base, extra = divmod(n_samples, k)
    folds = []
    start = 0
    for i in range(k):
        size = base + (1 if i < extra else 0)
        folds.append(indices[start:start + size])
        start += size

    splits = []
    for i in range(k):
        test_indices = list(folds[i])
        train_indices = [idx for j in range(k) if j != i for idx in folds[j]]
        splits.append((train_indices, test_indices))

    return splits
    pass