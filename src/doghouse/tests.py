from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Pets
from .serializers import PetsSerializer

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_pet(pet_foto=None, especie="", porte="", nome="", idade="", raca="", obs=""):
        Pets.objects.create(pet_foto=pet_foto, especie=especie, porte=porte, nome=nome, idade=idade, raca=raca, obs=obs)

    def setUp(self):
        # add test data
        self.create_pet(None, 'C', 'Gd', "Rex", 'A', "Vira-lata", "Cão adulto super dócil")
        self.create_pet(None, 'G', 'Pq', "Salem", 'F', "Vira-lata", "Filhote não vacinado")
        self.create_pet(None, 'C', 'Md', "Toby", 'F', "Vira-lata", "Filhote vacinado - 40 dias de vida")

class GetAllPets(BaseViewTest):
    def test_get_all_pets(self):
        response = self.client.get(
            reverse("pets-all", kwargs={"version": "v1"})
        )
        expected = Pets.objects.all()
        serialized = PetsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
