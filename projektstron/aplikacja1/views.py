from django.shortcuts import render
from .models import produkt, koszyk
def views_strona_glowna(request):
    #request.user.is_authenticated
    dane_z_modelu = produkt.objects.all()
    return render(request, 'strona_glowna.html',context={"dane_z_modelu":dane_z_modelu})

def views_strona_kazdego_produktu(request,id):
    dane_z_modelu = produkt.objects.get(id=id)
    return render(request, 'strona_kazdego_produktu.html',context={"dane_z_modelu":dane_z_modelu})

def views_koszyk(request,zakup):
    koszyk.objects.create(
        kupujacy = request.user.username,
        zamowiony_produkt = zakup
    )
    return render(request, 'koszyk.html',context={"zakup":zakup})
# def views_podsumowanie():
#     koszyk.objects.create(
#         kupujcy=request.user.username,
#         zamowony_produkt=zakup
#     )
