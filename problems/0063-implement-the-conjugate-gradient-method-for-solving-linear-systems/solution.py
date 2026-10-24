import numpy as np

def conjugate_gradient(A, b, n, x0=None, tol=1e-8):
    """
    Solve the system Ax = b using the Conjugate Gradient method.

    :param A: Symmetric positive-definite matrix
    :param b: Right-hand side vector
    :param n: Maximum number of iterations
    :param x0: Initial guess for solution (default is zero vector)
    :param tol: Convergence tolerance
    :return: Solution vector x
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    
    # Handle initial guess
    if x0 is None:
        x = np.zeros_like(b, dtype=float)
    else:
        x = np.array(x0, dtype=float)
        
    # Calculate initial residual vector and search direction
    r = b - np.dot(A, x)
    p = r.copy()
    rsold = np.dot(r, r)
    
    for _ in range(n):
        # Check for convergence if residual norm is smaller than tolerance
        if np.sqrt(rsold) < tol:
            break
            
        Ap = np.dot(A, p)
        alpha = rsold / np.dot(p, Ap)
        
        # Update solution and residual
        x += alpha * p
        r -= alpha * Ap
        
        rsnew = np.dot(r, r)
        
        # Check convergence on new residual
        if np.sqrt(rsnew) < tol:
            break
            
        # Update search direction
        beta = rsnew / rsold
        p = r + beta * p
        rsold = rsnew
        
    return x
