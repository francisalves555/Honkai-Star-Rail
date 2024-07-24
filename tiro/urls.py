from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_banner/', views.cad_tiro_banner, name='cad_tiro_banner'),
    path('cadastro_arma/', views.cad_tiro_arma, name="cad_tiro_arma"),
    path('lista_tiros_personagens/', views.lista_tiros_personagens, name='lista_tiros_personagens'),
    path('lista_tiros_armas/', views.lista_tiros_armas, name='lista_tiros_armas'),
 


]
