from django.urls import path, include
from .views import ListCreatePetsView, PetsDetailView

urlpatterns = [
    path('pets/', ListCreatePetsView.as_view(), name='pets-list-create'),
    path('pets/<int:pk>/', PetsDetailView.as_view(), name='pets-detail')
]
