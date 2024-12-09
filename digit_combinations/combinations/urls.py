from django.urls import path
from . import views

urlpatterns = [
    path('', views.combinations_view, name='combinations'),
]
