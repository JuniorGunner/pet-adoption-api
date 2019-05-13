from django.shortcuts import render
from rest_framework import generics
from .models import Pets
from .serializers import PetsSerializer

# Create your views here.
class ListPetsView(generics.ListAPIView):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
