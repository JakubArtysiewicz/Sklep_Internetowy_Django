from django.db import models

# class zamowienia(models.Model):
#     uzytkownik = models.TextField()
#     = models
class zdjecie(models.Model):
    obraz = models.ImageField(upload_to='photos/')
class produkt(models.Model):
    nazwa = models.CharField(max_length=100, default="Null")
    opis = models.CharField(max_length=100, default="Null")
    cena = models.FloatField(default=0)
    obraz = models.ForeignKey(zdjecie, on_delete=models.SET_NULL, null=True, blank=True)

class koszyk(models.Model):
    kupujacy = models.CharField(max_length=100)
    zamowiony_produkt = models.CharField(max_length=100,default="Null")
    # zamowiony_produkt = models.ForeignKey(max_length=100, default="Null")

