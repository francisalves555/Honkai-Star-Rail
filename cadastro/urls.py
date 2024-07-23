from django.urls import path
from . import views


urlpatterns = [
    path('personagem/', views.personagem, name="personagem"),
    path('arma/', views.arma, name="arma"),
    path('reroll', views.reroll, name="reroll"),
    path('arma_reroll', views.arma_reroll, name="arma_reroll"),
]


