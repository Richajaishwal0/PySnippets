# matrix_multiplication.py
def matrix_addition(A, B):
    """
    Add two matrices A and B.

    Args:
        A (list of list of int/float): First matrix.
        B (list of list of int/float): Second matrix.

    Returns:
        list of list of int/float: The resulting matrix after addition.

    Raises:
        ValueError: If the dimensions of the two matrices are not the same.

    Example:
        >>> A = [[1, 2], [3, 4]]
        >>> B = [[5, 6], [7, 8]]
        >>> add_matrices(A, B)
        [[6, 8], [10, 12]]
    """
    # Check if the dimensions of the two matrices are the same
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("The dimensions of the two matrices must be the same.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    # Perform matrix addition
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]

    return result

def matrix_multiplication(A, B):
    """
    Multiply two matrices A and B.

    Args:
        A (list of list of int/float): First matrix.
        B (list of list of int/float): Second matrix.

    Returns:
        list of list of int/float: The resulting matrix after multiplication.

    Raises:
        ValueError: If the number of columns in A does not match the number of rows in B.

    Example:
        >>> A = [[1, 2, 3], [4, 5, 6]]
        >>> B = [[7, 8], [9, 10], [11, 12]]
        >>> matrix_multiply(A, B)
        [[58, 64], [139, 154]]
    """
    # Check if the number of columns in A matches the number of rows in B
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must match number of rows in B.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

def matrix_transpose(A):
    """
    Transpose a matrix A.

    Args:
        A (list of list of int/float):
            The matrix to be transposed.

    Returns:
        list of list of int/float:
            The transposed matrix.

    Example:
        >>> A = [[1, 2, 3], [4, 5, 6]]
        >>> transpose_matrix(A)
        [[1, 4], [2, 5], [3, 6]]
    """
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


# Example usage
if __name__ == "__main__":
    # Example usage of the function
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    result = matrix_multiplication(A, B)
    print(result)

    