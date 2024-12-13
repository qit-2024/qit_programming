from django.http import JsonResponse
import numpy as np

def quantum_eigen(request):
    if request.method == "POST":
        try:
            # Retrieve matrix input from the POST request
            matrix = request.POST.getlist("matrix[]")
            matrix = np.array([list(map(float, row.split(","))) for row in matrix])

            # Validate matrix (it must be square)
            rows, cols = matrix.shape
            if rows != cols:
                raise ValueError("The matrix must be square (NxN).")

            # Calculate eigenvalues and eigenvectors
            eigenvalues, eigenvectors = np.linalg.eig(matrix)

            # Format the result as lists
            eigenvalues = eigenvalues.tolist()
            eigenvectors = eigenvectors.tolist()

            # Return result as JSON
            return JsonResponse({
                "eigenvalues": eigenvalues,
                "eigenvectors": eigenvectors
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)
