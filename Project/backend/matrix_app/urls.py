from django.urls import path  
from .views import MatrixView, QuantumView

urlpatterns = [  
    path('eigenvalues/', MatrixView.eigenvalues, name='eigenvalues'),  
    path('determinant/', MatrixView.determinant, name='determinant'),  
    path('properties/', MatrixView.properties, name='properties'),  
    path('tensor/', MatrixView.tensor_product, name='tensor_product'),
    path('density-matrix/', QuantumView.density_matrix, name='density_matrix'), 
]