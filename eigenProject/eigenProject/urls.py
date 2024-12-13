from django.contrib import admin
from django.urls import path
from eigenApp.views import quantum_eigen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quantum-eigen/', quantum_eigen, name="quantum_eigen"),
]
