from django.shortcuts import render

from .services.quantum_operations import create_density_matrix
from .services.validators import validate_quantum_state
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.matrix_operations import MatrixOperationsService
from typing import Dict, Any
import numpy as np

class MatrixView:
    @staticmethod
    @api_view(['POST'])
    def eigenvalues(request) -> Response:
        try:
            matrix = request.data.get('matrix')
            result = MatrixOperationsService.calculate_eigenvalues(matrix)
            return Response(result, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': 'Internal Server Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @staticmethod
    @api_view(['POST'])
    def determinant(request) -> Response:
        try:
            matrix = request.data.get('matrix')
            result = MatrixOperationsService.calculate_determinant(matrix)
            return Response(
                {'determinant': result},
                status=status.HTTP_200_OK
            )
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': 'Internal Server Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @staticmethod
    @api_view(['POST'])
    def properties(request) -> Response:
        try:
            matrix = request.data.get('matrix')
            result = MatrixOperationsService.check_matrix_properties(matrix)
            return Response(result, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': 'Internal Server Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @staticmethod
    @api_view(['POST'])
    def tensor_product(request) -> Response:
        try:
            matrix_a = request.data.get('matrix_a')
            matrix_b = request.data.get('matrix_b')
            result = MatrixOperationsService.calculate_tensor_product(
                matrix_a, matrix_b
            )
            return Response(
                {'result': result},
                status=status.HTTP_200_OK
            )
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': 'Internal Server Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
class QuantumView:
    @staticmethod
    @api_view(['POST'])
    def density_matrix(request): 
        try:  
            data = request.data  
            state_vector = data.get('state_vector')  
            is_complex = data.get('is_complex', False)  

            if not state_vector:  
                return Response(  
                    {'error': 'State vector must be provided'},  
                    status=status.HTTP_400_BAD_REQUEST  
                )  

            if is_complex:  
                state_vector = [complex(x['real'], x['imag']) for x in state_vector]  
            else:  
                state_vector = [complex(x, 0) for x in state_vector]  


            is_valid, message = validate_quantum_state(state_vector)  
            if not is_valid:  
                return Response(  
                    {'error': message},  
                    status=status.HTTP_400_BAD_REQUEST  
                )  


            density_matrix = create_density_matrix(state_vector)  
            

            result = {  
                'density_matrix': [  
                    [{'real': x.real, 'imag': x.imag} for x in row]  
                    for row in density_matrix  
                ],  
                'properties': {  
                    'trace': float(np.trace(density_matrix).real),  
                    'is_hermitian': bool(np.allclose(density_matrix, density_matrix.conj().T)),  
                    'is_positive': bool(np.all(np.linalg.eigvals(density_matrix) >= -1e-10)),  
                    'purity': float(np.trace(density_matrix @ density_matrix).real)  
                }  
            }  
            
            return Response(result)  
        except Exception as e:  
            return Response(  
                {'error': f'Error in calculation density matrix: {str(e)}'},  
                status=status.HTTP_400_BAD_REQUEST
            )