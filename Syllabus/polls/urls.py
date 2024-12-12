from django.urls import path

from .views import get_input_matrix, index


urlpatterns = [
    path("", index, name="index"),
    path("get_input_matrix/", get_input_matrix, name="get_input_matrix")
]
