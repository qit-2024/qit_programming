from django import forms
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


def validate_zeros(value):
    if value > 0:
        if value != int(str(int(str(value)[::-1]))[::-1]):
            raise ValidationError("Ensure this value has not leading zeros.")
    else:
        raise ValidationError("Ensure this value is greater than or equal to 0.")


class GetInputNumbers(forms.Form):
    number_1 = forms.IntegerField(validators=[MaxValueValidator(10**100-1), validate_zeros])
    number_2 = forms.IntegerField(validators=[MaxValueValidator(10**100-1), validate_zeros])
