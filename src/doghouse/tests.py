from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Pets
from .serializers import PetsSerializer
import json

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_pet(pet_foto="", especie="", porte="", nome="", idade="", raca="", obs=""):
        Pets.objects.create(pet_foto=pet_foto, especie=especie, porte=porte, nome=nome, idade=idade, raca=raca, obs=obs)

    def make_a_request(self, kind="post", **kwargs):
        if kind == "post":
            return self.client.post(
                reverse(
                    "pets-list-create",
                    kwargs={
                        "version": kwargs["version"]
                    }
                ),
                data=json.dumps(kwargs["data"]),
                content_type='application/json'
            )
        elif kind == "put":
            return self.client.put(
                reverse(
                    "pets-detail",
                    kwargs={
                        "version": kwargs["version"],
                        "pk": kwargs["id"]
                    }
                ),
                data=json.dumps(kwargs["data"]),
                content_type='application/json'
            )
        else:
            return None

    def fetch_a_pet(self, pk=0):
        return self.client.get(
            reverse(
                "pets-detail",
                kwargs={
                    "version": "v1",
                    "pk": pk
                }
            )
        )

    def delete_a_pet(self, pk=0):
        return self.client.delete(
            reverse(
                "pets-detail",
                kwargs={
                    "version": "v1",
                    "pk": pk
                }
            )
        )

    def setUp(self):
        # add test data
        self.create_pet("01", 'C', 'Gd', "Rex", 'A', "Vira-lata", "Cão adulto super dócil")
        self.create_pet("02", 'G', 'Pq', "Salem", 'F', "Vira-lata", "Filhote não vacinado")
        self.create_pet("03", 'C', 'Md', "Toby", 'F', "Vira-lata", "Filhote vacinado - 40 dias de vida")

        self.valid_pet_id = 1
        self.invalid_pet_id = 100

        self.valid_data = {
            "pet_foto": "04",
            "especie": "C",
            "porte": "Md",
            "nome": "Pet Test",
            "idade": "A",
            "raca": "Vira-lata",
            "obs": "Sem mais detalhes"
        }
        self.invalid_data = {
            "pet_foto": None,
            "especie": "",
            "porte": "",
            "nome": "",
            "idade": "",
            "raca": "",
            "obs": ""
        }

#GET (All)
class GetAllPetsTest(BaseViewTest):
    def test_get_all_pets(self):
        response = self.client.get(
            reverse("pets-list-create", kwargs={"version": "v1"})
        )
        expected = Pets.objects.all()
        serialized = PetsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#GET (Single Pet)
class GetASinglePetTest(BaseViewTest):
    def test_get_a_pet(self):
        response = self.fetch_a_pet(self.valid_pet_id)
        expected = Pets.objects.get(pk=self.valid_pet_id)
        serialized = PetsSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test with a song that does not exist
        response = self.fetch_a_pet(self.invalid_pet_id)
        self.assertEqual(
            response.data["Atenção"],
            "Animal com id: 100 não existe"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#POST
class AddPetsTest(BaseViewTest):
    def test_create_a_pet(self):
        response = self.make_a_request(
            kind="post",
            version="v1",
            data=self.valid_data
        )
        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # test with invalid data
        response = self.make_a_request(
            kind="post",
            version="v1",
            data=self.invalid_data
        )
        self.assertEqual(
            response.data["Atenção"],
            "Preencha os campos obrigatórios"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#PUT
class UpdatePetsTest(BaseViewTest):
    def test_update_a_pet(self):
        response = self.make_a_request(
            kind="put",
            version="v1",
            id=2,
            data=self.valid_data
        )
        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.make_a_request(
            kind="put",
            version="v1",
            id=3,
            data=self.invalid_data
        )
        self.assertEqual(
            response.data["Atenção"],
            "Preencha os campos obrigatórios"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#DELETE
class DeletePetsTest(BaseViewTest):
    def test_delete_a_pet(self):
        response = self.delete_a_pet(1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.delete_a_pet(100)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
