from django.urls import path
from . import views

urlpatterns = [
    # path('', views.leetcode_problem_view, name='leetcode_problem'),
    path('leetcode/', views.leet_problem_204_view, name='leet_problem_204'),
    path('turing/', views.turing_machine_view, name='turing_machine'),
]