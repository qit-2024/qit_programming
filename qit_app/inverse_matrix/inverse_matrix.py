import numpy as np

from ast import literal_eval

from qit_app.inverse_matrix.my_exception import (InvalidInputDataException, InvalidInputDataLengthException,
                                                 InvalidInputDataMatrixNotSquareException)


def parse_input(input_data):
    try:
        data_list = literal_eval(input_data)
        if isinstance(data_list, list):
            data = [np.float32(x) for x in data_list]
        else:
            raise InvalidInputDataException(
                f"Failure:\nInvalid input data!\nRequired list of numbers. Please check brackets []")
    except InvalidInputDataException as err:
        raise err
    except Exception:
        raise InvalidInputDataException(
            f"Failure:\nInvalid input data!\nRequired list of numbers.")

    if len(data) == 0:
        raise InvalidInputDataLengthException(
            f"Failure:\nInvalid input data (data length is equal 0)!")

    dim = np.sqrt(len(data))
    if dim % 1 != 0:
        raise InvalidInputDataMatrixNotSquareException(
            f"Failure: The input matrix is not a square matrix!")
    else:
        dim = int(dim)

    return np.array(data, dtype=np.float32).reshape(dim, dim)


def get_dimension(matrix):

    return matrix.shape[0]


def find_determinant(matrix):
    dim = get_dimension(matrix)
    if dim == 1:

        return matrix[0, 0]

    elif dim == 2:

        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

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

    return np.transpose(matrix)


def find_inverse_matrix(matrix, determinant):
    dim = get_dimension(matrix)

    return np.array(matrix / determinant, dtype=np.float32).reshape(dim, dim)


def check_result(matrix, adjugate_matrix):
    product_matrix = np.matmul(matrix, adjugate_matrix) / find_determinant(matrix)

    return np.array_equal(product_matrix, np.identity(get_dimension(matrix)))


def calc_inverse_matrix(input_matrix):
    calc_output = [f"Input data:\n{input_matrix}"]

    # Parsing input data.
    try:
        matrix = parse_input(input_matrix)
    except Exception as err:
        calc_output.append(str(err.args[0]))

        return calc_output

    calc_output.append(f"Input matrix:\n{matrix}")

    # Calculating the determinant of a matrix.
    det_a = find_determinant(matrix)
    calc_output.append(f"Determinant:\n{det_a}")

    # Checking if the matrix is singular. (singularity for determinant equal 0)
    if det_a != 0:
        # Calculating the cofactor's matrix.
        cof_matrix = find_cofactors_matrix(matrix)
        calc_output.append(f"Cofactor\'s matrix:\n{cof_matrix}")

        # Calculating the adjugate matrix.
        adj_matrix = find_adjugate_matrix(cof_matrix)
        calc_output.append(f"Adjugate matrix:\n{adj_matrix}")

        # Calculating the inverse matrix.
        inv_matrix = find_inverse_matrix(adj_matrix, det_a)
        calc_output.append(f"Inverse matrix:\n{inv_matrix}")

        # Checking the result.
        is_valid = check_result(matrix, adj_matrix)
        calc_output.append(f"Result:\n{"correct" if is_valid else "incorrect"}")
    else:
        calc_output.append("Failure:\nThe input matrix is a singular matrix [det(A) = 0]."
                           " The inverse of such matrix is not defined!")

    return calc_output
