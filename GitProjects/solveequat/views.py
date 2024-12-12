from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect

from solveequat.forms import EquationAndOrder
from solveequat.forms import StepSizeAndNumber
from solveequat.models import firstinputholder
from solveequat.models import secondinputholder
from solveequat.models import thirdinputholder
from solveequat.forms import InitialConditions
from solveequat.rungekutta import Rungekutta

def firstinput(request):
    if request.method=='POST':
        form = EquationAndOrder(request.POST)



        if form.is_valid():
            #return HttpResponse(form)
            #firstinputholder=EquationAndOrder
            return redirect ('secondinput',equation=form.cleaned_data["equation"],order=form.cleaned_data["order"])
    else:
        form = EquationAndOrder()

    return render(request,
                  'myfirst.html',
                  {'form': form})

def secondinput(request, equation, order):
    if request.method=='POST':
        form = StepSizeAndNumber(request.POST)

        if form.is_valid():
            #return HttpResponse(form)
            return redirect('thirdinput', equation=equation, order=order, step_size=form.cleaned_data["step_size"], step_number=form.cleaned_data["step_number"])
    else:
        print (equation)
        print (order)
        form = StepSizeAndNumber()

    return render(request,
                  'myfirst.html',
                  {'form': form})

def thirdinput(request, equation, order, step_size, step_number):
    step_size=float(step_size)
    if request.method=='POST':
        form = InitialConditions(request.POST,order=order)

        if form.is_valid():
            init_conditions=[form.cleaned_data["x_init"]]
            for i in range(0, order):
                init_conditions.append(form.cleaned_data[f"y{i}_init"])
            print(init_conditions)
            #initial={"x_init":8.7,"y0_init":152}
            #form = InitialConditions(order=order,initial=initial)
            Rungekutta(equation=equation, order=order, step_size=step_size, step_number=step_number, init_conditions=init_conditions)
            return HttpResponse(form)
    else:

        form = InitialConditions(order=order)

    return render(request,
                  'myfirst.html',
                  {'form': form})