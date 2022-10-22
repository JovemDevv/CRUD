from django.db import models

# Create your models here.

class Client(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.Datefield(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome