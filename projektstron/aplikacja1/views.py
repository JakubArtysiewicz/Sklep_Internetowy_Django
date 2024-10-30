from django.shortcuts import render
from .models import produkt
def views_strona_glowna(request):
    #request.user.is_authenticated
    dane_z_modelu = produkt.objects.all()
    return render(request, 'strona_glowna.html',context={"dane_z_modelu":dane_z_modelu})

def views_strona_kazdego_produktu(request,id):
    dane_z_modelu = produkt.objects.get(id=id)
    return render(request, 'strona_kazdego_produktu.html',context={"dane_z_modelu":dane_z_modelu})