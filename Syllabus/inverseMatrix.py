# TODO: add comments and doc
import numpy
import numpy as np


def parse_input(data):
    if len(data) == 0:
        # TODO: raise exception
        print(f"Failure: Invalid input data [data length is equal 0]!")

    dim = numpy.sqrt(len(data))
    if dim % 1 != 0:
        # TODO: raise exception
        print(f"Failure: The input matrix is not a square matrix!")
    else:
        dim = int(dim)

    return np.array(data, dtype=np.float32).reshape(dim, dim)


def get_dimension(matrix):

    return matrix.shape[0]


def find_determinant(matrix):
    # numpy.linalg.det() can be used instead of this function.
    # return np.linalg.det(matrix)

    dim = get_dimension(matrix)
    if dim == 1:

        return matrix[0, 0]

    elif dim == 2:

        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    # # Usage of Rule of Sarrus (redundant due to usage of recursion in "else" case)
    # elif dim == 3:
    #     det = 0
    #     order_x = list(range(dim))
    #     for order, sign in zip([order_x, order_x[::-1]], [1, -1]):
    #         for shift in range(dim):
    #             product = 1
    #             order_y = order[shift:] + order[0:shift] if shift != 0 else order
    #             for ix, iy in zip(order_x, order_y):
    #                 product *= matrix[ix, iy]
    #                 if product == 0:
    #                     break
    #             det += sign * product
    else:
        det = 0
        ix = 0
        for iy in range(dim):
            minor_matrix = np.delete(np.delete(matrix, ix, axis=0), iy, axis=1)
            det += np.power(-1, ix + iy) * matrix[ix, iy] * find_determinant(minor_matrix)

    return det


def find_cofactors_matrix(matrix):
    dim = get_dimension(matrix)
    if dim == 1:
        tmp = [1]
    else:
        tmp = []
        for ix in range(dim):
            for iy in range(dim):
                minor_matrix = np.delete(np.delete(matrix, ix, axis=0), iy, axis=1)
                cofactor = np.power(-1, ix + iy) * find_determinant(minor_matrix)
                tmp.append(cofactor if cofactor != -0 else 0)

    return np.array(tmp, dtype=np.float32).reshape(dim, dim)


def find_adjugate_matrix(matrix):
    # TODO: add own implementation

    return np.transpose(matrix)


def find_inverse_matrix(matrix, determinant):
    dim = get_dimension(matrix)

    return np.array(matrix / determinant, dtype=np.float32).reshape(dim, dim)


def check_result(matrix, adjugate_matrix):
    product_matrix = np.matmul(matrix, adjugate_matrix) / find_determinant(matrix)

    return np.array_equal(product_matrix, np.identity(get_dimension(matrix)))


input_data = [1, 0, -3, 2, -2, 1, 0, -1, 3] # det = 1
output_data = [-5, 3, -6, -6, 3, -7, -2, 1, -2]
# input_data = [1, 2, 3, 0, 1, 4, 5, 6, 0] # det = 1
# output_data = [-24, 18, 5, 20, -15, -4, -5, 4, 1]
# input_data = [2, 5, 3, 7] # det = -1
# output_data = [-7, 5, 3, -2]
# input_data = [1, 0, 4, -6, 2, 5, 0, 3, -1, 2, 3, 5, 2, 1, -2, 3] # det = 318
# input_data = [1, -2, 0, 2, -1, 3, 1, -2, -1, 5, 3, -2, 0, 7, 7, 0] # det = 0
# input_data = [0, 0, -1, 2, 0, 1, 0, 0, 9, 0, 0, 0, 0, 0, 0, 1] # det = 9
# input_data = [2, 0, 0, 1, 5, 0, 2, 0, 1, 2, 0, 0, 2, 3, 1, 1, 1, 3, 0, 0, 5, 2, 1, 0, 0] # det = 460


#  TODO: catch parse_exception
# Parsing input data.
matrix_a = parse_input(input_data)
print(f"Input matrix:\n{matrix_a}")

# Calculating the determinant of a matrix.
det_a = find_determinant(matrix_a)
print(f"Determinant: {det_a}")

# Checking if the matrix is singular. (singularity for determinant equal 0)
if det_a != 0:
    # Calculating the cofactor's matrix.
    cof_matrix = find_cofactors_matrix(matrix_a)
    print(f"Cofactor's matrix:\n{cof_matrix}")

    # Calculating the adjugate matrix.
    adj_matrix = find_adjugate_matrix(cof_matrix)
    print(f"Adjugate matrix:\n{adj_matrix}")

    # Calculating the inverse matrix.
    inv_matrix = find_inverse_matrix(adj_matrix, det_a)
    print(f"Inverse matrix:\n{inv_matrix}")

    # Checking the result.
    result = check_result(matrix_a, adj_matrix)
    print(f"Result: {"correct." if result else "incorrect!"}")
else:
    print(f"Failure: The input matrix is a singular matrix [det(A) = 0]. The inverse of such matrix is not defined!")
