from django.urls import re_path

from .views import HomePage


urlpatterns = [
    re_path("", HomePage.as_view())
]
