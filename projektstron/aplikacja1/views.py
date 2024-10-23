from django.shortcuts import render
from .models import produkt
def views_strona_glowna(request):
    dane_z_modelu = produkt.objects.all()
    return render(request, 'strona_glowna.html',context={"dane_z_modelu":dane_z_modelu})