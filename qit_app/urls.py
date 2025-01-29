from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("leet_code/", views.leet_code, name="leet_code"),
    path("sorting_algorithms/", views.sorting_algorithms, name="sorting_algorithms"),
    path("inverse_matrix/", views.inverse_matrix, name="inverse_matrix")
]
