import math
import random

class MatrixDecomposition:
    @staticmethod
    def lu_decomposition(matrix):
        """
        Perform LU decomposition without using numpy
        Returns lower and upper triangular matrices
        """
        n = len(matrix)
        
        # Initialize L and U matrices
        L = [[0.0] * n for _ in range(n)]
        U = [[0.0] * n for _ in range(n)]
        
        for i in range(n):
            # Upper triangular matrix
            for k in range(i, n):
                sum = 0
                for j in range(i):
                    sum += L[i][j] * U[j][k]
                U[i][k] = matrix[i][k] - sum
            
            # Lower triangular matrix
            for k in range(i, n):
                if i == k:
                    L[i][i] = 1  # Diagonal of L is 1
                else:
                    sum = 0
                    for j in range(i):
                        sum += L[k][j] * U[j][i]
                    L[k][i] = (matrix[k][i] - sum) / U[i][i]
        
        return L, U

    @staticmethod
    def qr_decomposition(matrix):
        """
        Perform QR decomposition using Gram-Schmidt process
        Returns orthogonal matrix Q and upper triangular matrix R
        """
        def dot_product(a, b):
            return sum(x*y for x, y in zip(a, b))
        
        def vector_magnitude(a):
            return math.sqrt(sum(x*x for x in a))
        
        def scalar_multiply(scalar, vector):
            return [scalar * x for x in vector]
        
        def vector_subtract(a, b):
            return [x - y for x, y in zip(a, b)]
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Transpose matrix for easier column operations
        A = list(map(list, zip(*matrix)))
        
        Q = []
        R = [[0.0] * n for _ in range(n)]
        
        for i in range(n):
            # Current column
            u = A[i]
            
            # Subtract projections of previous orthogonal vectors
            for j in range(len(Q)):
                r_ji = dot_product(A[i], Q[j])
                R[j][i] = r_ji
                u = vector_subtract(u, scalar_multiply(r_ji, Q[j]))
            
            # Normalize the vector
            r_ii = vector_magnitude(u)
            R[i][i] = r_ii
            
            # Avoid division by zero
            if r_ii != 0:
                Q.append(scalar_multiply(1/r_ii, u))
            else:
                Q.append(u)
        
        # Transpose Q back to match input matrix orientation
        Q = list(map(list, zip(*Q)))
        
        return Q, R
