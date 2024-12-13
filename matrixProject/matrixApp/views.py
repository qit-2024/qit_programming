from django.http import JsonResponse
import numpy as np

def matrix_operations(request):
    if request.method == "POST":
        try:
            # Input dimensions for matrices
            rows1 = int(request.POST.get("rows1"))
            cols1 = int(request.POST.get("cols1"))
            rows2 = int(request.POST.get("rows2"))
            cols2 = int(request.POST.get("cols2"))
            operation = request.POST.get("operation")  # add, subtract, multiply, divide

            # Create first matrix
            matrix1 = [
                list(map(float, request.POST.getlist(f"matrix1_row{i}[]")))
                for i in range(rows1)
            ]

            # Create second matrix
            matrix2 = [
                list(map(float, request.POST.getlist(f"matrix2_row{i}[]")))
                for i in range(rows2)
            ]

            # Convert to NumPy arrays
            matrix1 = np.array(matrix1)
            matrix2 = np.array(matrix2)

            # Perform the operation
            result = None
            if operation == "add":
                if matrix1.shape == matrix2.shape:
                    result = np.add(matrix1, matrix2).tolist()
                else:
                    raise ValueError("Addition requires matrices of the same dimensions.")
            elif operation == "subtract":
                if matrix1.shape == matrix2.shape:
                    result = np.subtract(matrix1, matrix2).tolist()
                else:
                    raise ValueError("Subtraction requires matrices of the same dimensions.")
            elif operation == "multiply":
                if cols1 == rows2:
                    result = np.matmul(matrix1, matrix2).tolist()
                else:
                    raise ValueError("Multiplication requires cols1 of matrix1 to equal rows2 of matrix2.")
            elif operation == "divide":
                if matrix1.shape == matrix2.shape:
                    result = np.divide(matrix1, matrix2).tolist()
                else:
                    raise ValueError("Division requires matrices of the same dimensions.")
            else:
                raise ValueError("Invalid operation specified.")

            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)
