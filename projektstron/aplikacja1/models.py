from django.db import models

class produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(max_length=100)

