from django import forms

class EquationAndOrder(forms.Form):
    equation = forms.CharField()
    order = forms.IntegerField()

class StepSizeAndNumber(forms.Form):
    step_size = forms.FloatField()
    step_number = forms.IntegerField()

class InitialConditions(forms.Form):
    x_init = forms.FloatField()

    def __init__(self,*args,**kwargs):
        order=kwargs.pop("order")
        super().__init__(*args,**kwargs)
        for i in range (0, order):
            self.fields[f"y{i}_init"]=forms.FloatField()
