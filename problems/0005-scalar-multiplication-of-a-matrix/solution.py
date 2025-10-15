import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    mat = np.array(matrix)
    result = np.dot(mat,scalar)
	return result.tolist()