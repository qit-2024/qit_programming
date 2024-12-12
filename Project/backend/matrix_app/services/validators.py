from typing import List, Union, Tuple
import numpy as np

def validate_matrix(matrix: List[List[float]]) -> None:
    if not matrix or not isinstance(matrix, list):
        raise ValueError("The matrix must not be an empty list.")
    
    if not all(isinstance(row, list) for row in matrix):
        raise ValueError("All rows of the matrix must be lists")
    
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise ValueError("All rows of a matrix must have the same length")
    
    try:
        np.array(matrix, dtype=float)
    except:
        raise ValueError("All elements of the matrix must be numbers")

def validate_square_matrix(matrix: List[List[float]]) -> None:
    validate_matrix(matrix)
    
    if len(matrix) != len(matrix[0]):
        raise ValueError("The matrix must be square")
    
def validate_quantum_state(state_vector: List[Union[float, complex]]) -> Tuple[bool, str]:  
    """  
    Проверяет корректность квантового состояния  
    """  
    try:  
        state = np.array(state_vector, dtype=complex)  
        norm = np.linalg.norm(state)  
        
        # Проверка нормировки (с небольшой погрешностью)  
        if not np.isclose(norm, 1.0, atol=1e-10):  
            return False, f"Вектор состояния должен быть нормирован. Текущая норма: {norm}"  
        
        return True, "Состояние корректно"  
    except Exception as e:  
        return False, f"Ошибка валидации: {str(e)}" 