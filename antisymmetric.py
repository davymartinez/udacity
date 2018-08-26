# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    matrix_length = len(A)

    # Check if the list is square by comparing its overall length to each row's
    # length
    for row in A:
        if len(row) != matrix_length:
            return False

    # Iterate over the nested list comparing pairs of items -- a antisymmetric
    # list (or matrix) should be of the form A[i][j] == -A[j][i]
    for i in range(matrix_length):
        for j in range(matrix_length):
            if A[i][j] != -A[j][i]:
                return False

    return True

# Test Cases:

print(antisymmetric([[0, 1, 2],
                    [-1, 0, 3],
                    [-2, -3, 0]]))
#>>> True

print(antisymmetric([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]))
#>>> True

print(antisymmetric([[0, 1, 2],
                    [-1, 0, -2],
                    [2, 2,  3]]))
#>>> False

print(antisymmetric([[1, 2, 5],
                    [0, 1, -9],
                    [0, 0, 1]]))
#>>> False
