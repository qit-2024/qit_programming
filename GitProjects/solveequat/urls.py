from django.urls import path
from . import views

urlpatterns = [
    path('firstinput/', views.firstinput, name='firstinput'),
    path('secondinput/<str:equation>/<int:order>', views.secondinput, name='secondinput'),
    path('thirdinput/<str:equation>/<int:order>/<int:step_number>/<str:step_size>', views.thirdinput, name='thirdinput'),
]
# Create your views here.
