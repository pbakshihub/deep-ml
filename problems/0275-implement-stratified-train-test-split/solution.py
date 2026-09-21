import numpy as np

def stratified_train_test_split(X, y, test_size, random_seed=None):
    """
    Split data into train and test sets while maintaining class proportions.
    
    Args:
        X: Feature matrix of shape (n_samples, n_features)
        y: Label vector of shape (n_samples,)
        test_size: Proportion of data for test set (0 < test_size < 1)
        random_seed: Random seed for reproducibility
    
    Returns:
        X_train, X_test, y_train, y_test
    """
    X = np.asarray(X)
    y = np.asarray(y)
    if X.shape[0] != y.shape[0]:
        raise ValueError("X and y must have the same number of samples.")
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1 (exclusive).")

    rng = np.random.RandomState(random_seed)
    classes = np.unique(y)

    train_idx, test_idx = [], []
    for c in classes:
        cls_idx = np.where(y == c)[0]
        rng.shuffle(cls_idx)

        # Floor the per-class test count
        n_test = int(len(cls_idx) * test_size)

        test_idx.extend(cls_idx[:n_test])
        train_idx.extend(cls_idx[n_test:])

    train_idx = rng.permutation(np.array(train_idx, dtype=int))
    test_idx = rng.permutation(np.array(test_idx, dtype=int))

    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
