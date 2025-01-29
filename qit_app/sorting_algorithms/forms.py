from django import forms
from django.contrib.postgres.forms import SimpleArrayField


class GetInputList(forms.Form):
    input_list = SimpleArrayField(forms.IntegerField())
