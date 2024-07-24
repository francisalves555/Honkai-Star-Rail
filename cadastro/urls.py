from django.urls import path
from . import views


urlpatterns = [
    path('personagens/', views.personagem, name="personagem"),
    path('armas/', views.arma, name="arma"),
    path('personagens_reroll', views.reroll, name="reroll"),
    path('arma_reroll', views.arma_reroll, name="arma_reroll"),
]


