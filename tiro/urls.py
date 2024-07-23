from django.urls import path
from . import views

urlpatterns = [
    path('cad_tiro_banner/', views.cad_tiro_banner, name='cad_tiro_banner'),
    path('cad_tiro_arma/', views.cad_tiro_arma, name="cad_tiro_arma"),
    path('lista_tiros_personagens/', views.lista_tiros_personagens, name='lista_tiros_personagens'),
    path('lista_tiros_armas/', views.lista_tiros_armas, name='lista_tiros_armas'),
    path('ed_tiro_personagem/<int:id>', views.ed_tiro_personagem, name='ed_tiro_personagem'),
    path('ed_tiro_arma/<int:id>', views.ed_tiro_arma, name='ed_tiro_arma'),
    path('del_tiro_personagem/<int:id>', views.del_tiro_personagem, name='del_tiro_personagem'),
    path('del_tiro_arma/<int:id>', views.del_tiro_arma, name='del_tiro_arma'),


]
