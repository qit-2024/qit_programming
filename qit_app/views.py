import markdown

from django.shortcuts import render

from qit_app.leet_code.forms import GetInputNumbers
from qit_app.leet_code.utils import list_node_to_int, int_to_list_node
from qit_app.leet_code.add_two_numbers_recursion import Solution
from qit_app.sorting_algorithms.forms import GetInputList
from qit_app.sorting_algorithms.sorting_algorithms import compare_sorts
from qit_app.inverse_matrix.forms import GetInputMatrix
from qit_app.inverse_matrix.inverse_matrix import calc_inverse_matrix
from qit_app.utils import parse_data_for_html


def index(request):
    with open("README.md", "r") as f:
        f_data = f.read()

    data = markdown.markdown(f_data)

    return render(request, "index.html", {"readme": data})


def leet_code(request):
    context = dict()
    form = GetInputNumbers(request.POST or None)
    context["form"] = form
    if request.POST:
        if form.is_valid():
            n1 = form.cleaned_data.get("number_1")
            n2 = form.cleaned_data.get("number_2")
            l1 = int_to_list_node(n1)
            l2 = int_to_list_node(n2)
            result = list_node_to_int(Solution.add_two_numbers(l1, l2))
            data = [f"Input number 1:\n{n1}",
                    f"Input number 2:\n{n2}",
                    f"Output:\n{str(result)}"]
            context["calc_output"] = parse_data_for_html(data)
            context["form"] = GetInputNumbers(None)

    return render(request, "leet_code.html", context)


def sorting_algorithms(request):
    context = dict()
    form = GetInputList(request.POST or None)
    context["form"] = form
    if request.POST:
        if form.is_valid():
            l = form.cleaned_data.get("input_list")
            context["sorted_output"], context["comparison"] = compare_sorts(l)

    return render(request, "sorting_algorithms.html", context)


def inverse_matrix(request):
    data = None
    if request.method == "POST":
        form = GetInputMatrix(request.POST)
        if form.is_valid():
            input_matrix = form.data["input_matrix_field"]
            if input_matrix:
                data = parse_data_for_html(calc_inverse_matrix(input_matrix))
            else:
                data = [["Please insert a matrix."]]

    return render(request, "inverse_matrix.html", {"calc_output": data})
