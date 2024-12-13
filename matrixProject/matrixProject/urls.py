from django.contrib import admin
from django.urls import path
from matrixApp.views import matrix_operations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('matrix/', matrix_operations, name="matrix_operations"),
]
