from django.urls import path
from .views import *
urlpatterns = [
    path('', views_strona_glowna),
    path('<int:id>',views_strona_kazdego_produktu)
]