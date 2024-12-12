from django.shortcuts import render
from .forms import LeetProblem204Form
from .forms import TuringMachineForm

from .leet_code_solution import LeetcodeSolution
from .turing_machine import TuringMachine 


def leet_problem_204_view(request):
    context = {}
    if request.method == 'POST':
        form = LeetProblem204Form(request.POST)
        
        if form.is_valid():
            num = int(form.cleaned_data['user_input'])
            print(num)
            res = LeetcodeSolution.countPrimes(num)
            context['result'] = str(res)
        else:
            context['errors'] = form.errors
    else:
        form = LeetProblem204Form()
    
    context['form'] = form
    return render(request, 'leet_problem_204.html', context)



def turing_machine_view(request):
    """
    View to handle Turing Machine code input and simulation
    """
    context = {}
    
    if request.method == 'POST':
        # Create a form instance with POST data
        form = TuringMachineForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            try:
                # Get the cleaned input data
                turing_code = form.cleaned_data['turing_code']
                initial_tape = form.cleaned_data['initial_tape'] or ''
                
                # Create Turing Machine instance and run
                turing_machine = TuringMachine(turing_code)
                status, steps, tape = turing_machine.simulate(initial_tape)

                print(status, steps, tape)
                
                # Populate context with simulation results
                context['result'] = status
                context['final_tape'] = tape
                context['step_count'] = len(steps)
                
            except Exception as e:
                context['turing_error'] = str(e)
        else:
            # If form validation fails, errors will be in the form
            context['form_errors'] = form.errors
    else:
        # If it's a GET request, create a blank form
        form = TuringMachineForm()
    
    # Always add the form to the context
    context['form'] = form
    return render(request, 'turing_machine.html', context)