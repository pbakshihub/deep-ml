import numpy as np

def impute(X: np.ndarray) -> np.ndarray:
    '''
    Fill in missing values (NaN) in the input array.
    
    Args:
        X: Array with possible NaN values, shape (n_samples, n_features)
    
    Returns:
        X_clean: Array with no NaN values, same shape as X
    '''
    
    
    # TODO: Fill in NaN values
    X_imputed = X.copy()
    
    # Compute column medians ignoring NaNs
    col_medians = np.nanmedian(X_imputed, axis=0)
    
    # Find indices where values are NaN
    nan_indices = np.where(np.isnan(X_imputed))
    
    # Replace NaNs with corresponding column median
    X_imputed[nan_indices] = col_medians[nan_indices[1]]
    
    return X_imputed
    
    
