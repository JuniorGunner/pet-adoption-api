from django.shortcuts import render
from rest_framework import generics
from .models import Pets
from .serializers import PetsSerializer
#from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

# Create your views here.
class ListCreatePetsView(generics.ListAPIView):
    """
    GET pets/
    POST pets/
    """
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer

    def post(self, request, *args, **kwargs):
        a_pet = Pets.objects.create(
            pet_foto=request.data["pet_foto"],
            especie=request.data["especie"],
            porte=request.data["porte"],
            nome=request.data["nome"],
            idade=request.data["idade"],
            raca=request.data["raca"],
            obs=request.data["obs"]
        )
        return Response(
            data=PetsSerializer(a_pet).data,
            status=status.HTTP_201_CREATED
        )

class PetsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET pets/:id/
    PUT pets/:id/
    DELETE pets/:id/
    """
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_pet = self.queryset.get(pk=kwargs["pk"])
            return Response(PetsSerializer(a_pet).data)
        except Pets.DoesNotExist:
            return Response(
                data={
                    "Atenção": "Animal com id: {} não existe".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        try:
            a_pet = self.queryset.get(pk=kwargs["pk"])
            serializer = PetsSerializer()
            updated_pet = serializer.update(a_pet, request.data)
            return Response(PetsSerializer(updated_pet).data)
        except Pets.DoesNotExist:
            return Response(
                data={
                    "Atenção": "Animal com id: {} não existe".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_pet = self.queryset.get(pk=kwargs["pk"])
            a_pet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pets.DoesNotExist:
            return Response(
                data={
                    "Atenção": "Animal com id: {} não existe".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
