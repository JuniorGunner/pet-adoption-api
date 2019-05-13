from django.urls import path, include
from .views import ListPetsView

urlpatterns = [
    path('pets/', ListPetsView.as_view(), name='pets-all')
]
