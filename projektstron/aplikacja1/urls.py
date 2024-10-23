from django.urls import path
from .views import views_strona_glowna
urlpatterns = [
    path('', views_strona_glowna)
]