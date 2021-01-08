from django.db import models

# Creating a model for our users.

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    senha = models.CharField(max_length=8)
    celular = models.CharField(max_length=14)
    cpf = models.CharField(max_length=13)
