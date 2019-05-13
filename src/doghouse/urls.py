from django.urls import path, include
from .views import ListCreatePetsView, PetsDetailView

urlpatterns = [
    path('pets/', ListCreatePetsView.as_view(), name='pets-all'),
    path('pets/<int:pk>/', PetsDetailView.as_view(), name='pets-detail')
]
