import numpy as np
from numpy import linalg as LA
from typing import Tuple, Dict, List, Union
from .validators import validate_matrix, validate_square_matrix

class MatrixOperationsService:
    @staticmethod
    def calculate_eigenvalues(matrix: List[List[float]]) -> Dict[str, Union[List[complex], List[List[complex]]]]:
        try:
            validate_square_matrix(matrix)
            matrix_np = np.array(matrix, dtype=float)
            eigenvalues, eigenvectors = LA.eig(matrix_np)
            
            return {
                'eigenvalues': eigenvalues.tolist(),
                'eigenvectors': eigenvectors.tolist()
            }
        except Exception as e:
            raise ValueError(f"Error in calculating eigenvalues: {str(e)}")

    @staticmethod
    def calculate_determinant(matrix: List[List[float]]) -> float:
        try:
            validate_square_matrix(matrix)
            matrix_np = np.array(matrix, dtype=float)
            return float(LA.det(matrix_np))
        except Exception as e:
            raise ValueError(f"Error in calculating the determinant: {str(e)}")

    @staticmethod
    def check_matrix_properties(matrix: List[List[float]]) -> Dict[str, bool]:
        try:
            validate_square_matrix(matrix)
            matrix_np = np.array(matrix, dtype=float)
            

            is_symmetric = np.allclose(matrix_np, matrix_np.T)
            

            try:
                is_orthogonal = np.allclose(
                    matrix_np.dot(matrix_np.T),
                    np.eye(len(matrix_np))
                )
            except:
                is_orthogonal = False
            
            return {
                'is_symmetric': bool(is_symmetric),
                'is_orthogonal': bool(is_orthogonal)
            }
        except Exception as e:
            raise ValueError(f"Error checking matrix properties: {str(e)}")

    @staticmethod
    def calculate_tensor_product(
        matrix_a: List[List[float]], 
        matrix_b: List[List[float]]
    ) -> List[List[float]]:

        try:
            validate_matrix(matrix_a)
            validate_matrix(matrix_b)
            
            matrix_a_np = np.array(matrix_a, dtype=float)
            matrix_b_np = np.array(matrix_b, dtype=float)
            
            result = np.kron(matrix_a_np, matrix_b_np)
            return result.tolist()
        except Exception as e:
            raise ValueError(f"Error while calculating tensor product: {str(e)}")