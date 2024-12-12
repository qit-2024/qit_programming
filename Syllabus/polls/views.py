from django.shortcuts import render

from .forms import GetInputMatrix
from .inverse_matrix import calc_inverse_matrix
from .utils import parse_data_for_html

def get_input_matrix(request):
    data = None
    if request.method == "POST":
        form = GetInputMatrix(request.POST)
        if form.is_valid():
            input_matrix = form.data["input_matrix_field"]
            if input_matrix:
                data = parse_data_for_html(calc_inverse_matrix(input_matrix))
            else:
                data = [["Please insert a matrix."]]

    return render(request, "index.html", {"calc_output": data})


def index(request):

    return render(request, "index.html")
