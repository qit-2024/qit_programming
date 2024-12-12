import numpy as np  
from typing import List

def create_density_matrix(state_vector: List[complex]) -> np.ndarray:  
    """  
    Создает матрицу плотности из вектора состояния.  
    ρ = |ψ⟩⟨ψ|  
    """  
    state = np.array(state_vector, dtype=complex)  
    # Нормализация вектора состояния  
    state = state / np.linalg.norm(state)  
    # Создание матрицы плотности  
    return np.outer(state, state.conj())  
 