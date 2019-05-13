# Generated by Django 2.2.1 on 2019-05-13 14:00

from django.db import migrations, models
import django.db.models.deletion
import doghouse.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_foto', models.ImageField(blank=True, null=True, upload_to=doghouse.models.get_image_path)),
                ('especie', models.CharField(choices=[('C', 'C'), ('G', 'G')], default='C', max_length=1)),
                ('porte', models.CharField(choices=[('Pq', 'Pequeno'), ('Md', 'Médio'), ('Gd', 'Grande')], default='Gd', max_length=2)),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.CharField(choices=[('F', 'Filhote'), ('A', 'Adulto')], default='A', max_length=1)),
                ('raca', models.CharField(max_length=100)),
                ('obs', models.TextField(blank=True, max_length=500, null=True)),
                ('pet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doghouse.Pets', unique=True)),
            ],
        ),
    ]
