from django.db import models

# Create your models here.
class firstinputholder(models.Model):
    equation = models.fields.CharField(max_length=50)
    order = models.fields.IntegerField()

class secondinputholder(models.Model):
    step_size = models.fields.FloatField()
    step_number = models.fields.IntegerField()

class thirdinputholder(models.Model):
    x_init = models.fields.FloatField()
    y_init = models.fields.FloatField()

    #order = int(firstinputholder.order)
    #steps = int(secondinputholder.step_number)

    #derivatives=numpy.zeros([order + 1, steps + 1])
    #for i in range(0, order):
           # dy_init[i] = models.fields.FloatField()
