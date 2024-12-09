from django.shortcuts import render
from itertools import product

# Define the mappings for digits 2 to 9
digit_to_letters = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
}

def combinations_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('digits')
        try:
            digits = [int(d) for d in user_input]
            if len(digits) == 4 and all(digit in digit_to_letters for digit in digits):
                lists_of_letters = [digit_to_letters[digit] for digit in digits]
                combinations = [''.join(combo) for combo in product(*lists_of_letters)]
                return render(request, 'combinations.html', {'combinations': combinations})
            else:
                error = "Invalid input. Please enter only 4 digits from 2 to 9."
        except (IndexError, ValueError):
            error = "Invalid input. Please enter exactly 4 digits."
        return render(request, 'combinations.html', {'error': error})
    
    return render(request, 'combinations.html')
