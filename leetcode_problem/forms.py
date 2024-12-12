from django import forms
from django.core.validators import (
    MinLengthValidator, 
    MaxLengthValidator, 
    RegexValidator
)

class LeetProblem204Form(forms.Form):
    user_input = forms.CharField(
        label='',
        max_length=100,
    
  validators=[
            # Ensure minimum length of 3 characters
            MinLengthValidator(1, message="Please input a number"),
            # Regex validator to allow only letters and spaces
            RegexValidator(
                regex=r'^[0-9]', 
                message="Only numbers are allowed"
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter a number',
            'class': 'form-control'
        })
    )


class TuringMachineForm(forms.Form):
    turing_code = forms.CharField(
        label='Enter Turing Machine Code',
        widget=forms.Textarea(attrs={
            'placeholder': 'Paste your Turing Machine code here...',
            'class': 'form-control',
            'rows': 10
        }),
        validators=[
            MinLengthValidator(1, message="Turing Machine code cannot be empty")
        ]
    )

    # Optional: Add a field for initial tape input
    initial_tape = forms.CharField(
        label='Initial Tape Input (optional)',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter initial tape contents',
            'class': 'form-control'
        })
    )