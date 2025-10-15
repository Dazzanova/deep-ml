import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	a_np = np.array(a)
	b_np = np.array(b)

	if a_np.shape[1] != b_np.shape[0]:
		return -1
	

	result = np.dot(a_np, b_np)
	return result.tolist()