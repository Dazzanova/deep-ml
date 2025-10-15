
import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Convert input lists to numpy arrays
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)
    
    # Use the normal equation: θ = (XᵀX)^(-1) Xᵀy
    theta = np.linalg.pinv(X.T @ X) @ X.T @ y  # pseudo-inverse for stability
    
    # Round coefficients to 4 decimal places
    theta = np.round(theta, 4)
    
    # Return as list
    return theta.tolist()
