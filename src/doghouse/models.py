from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('pics', str(instance.id), filename)

# Create your models here.
class Pets(models.Model):
    pet = models.ForeignKey('PET', unique=True, models.SET_NULL, blank=True, null=True)
    pet_foto = ImageField(upload_to=get_image_path, blank=True, null=True)

    CACHORRO = 'C'
    GATO = 'G'
    ESPECIE_CHOICES = (
        (CACHORRO, 'C'),
        (GATO, 'G')
    )
    especie = models.CharField(max_length=1, choices=ESPECIE_CHOICES, default=CACHORRO)

    PEQ = 'Pq'
    MED = 'Md'
    GDE = 'Gd'
    PORTE_CHOICES = (
        (PEQ, 'Pequeno'),
        (MED, 'Médio'),
        (GDE, 'Grande')
    )
    porte = models.CharField(max_length=2, choices=PORTE_CHOICES, default=GDE)

    FILHOTE = 'F'
    ADULTO = 'A'
    IDADE_CHOICES = (
        (FILHOTE, 'Filhote'),
        (ADULTO, 'Adulto')
    )

    nome = models.CharField(max_length=50, null=False)
    idade = models.CharField(max_length=1, choices=IDADE_CHOICES, default=ADULTO)
    raca = models.CharField(max_length=100, null=False)
    obs = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "pet_foto: {}\nEspecie: {}\nPorte: {}\nNome: {}\nIdade: {}\nRaça: {}\nObs.: {}"\
        .format(self.pet_foto, self.especie, self.porte, self.nome, self.idade, self.raca, self.obs)
