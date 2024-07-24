from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('personagem/<int:id>', views.ed_personagem, name='ed_personagem'),
    path('arma/<int:id>', views.ed_arma, name="ed_arma"),
    path('lista_personagens/', views.lista_personagens, name='lista_personagens'),
    path('lista_personagens_reroll/', views.lista_reroll_personagens, name='lista_reroll_personagens'),
    path('del_personagem/<int:id>', views.del_personagem, name='del_personagem'),
    path('del_personagem_reroll/<int:id>', views.del_OC_personagem, name='del_OC_personagem'),
    path('lista_armas/', views.lista_armas, name='lista_armas'),
    path('lista_armas_reroll/', views.lista_arma_reroll, name="lista_arma_reroll"),
    path('del_arma/<int:id>',views.del_arma, name='del_arma'),
    path('del_arma_r/<int:id>', views.del_OC_arma, name="del_OC_arma"),
    path('tiro_personagem/<int:id>', views.ed_tiro_personagem, name='ed_tiro_personagem'),
    path('tiro_arma/<int:id>', views.ed_tiro_arma, name='ed_tiro_arma'),
    path('del_tiro_personagem/<int:id>', views.del_tiro_personagem, name='del_tiro_personagem'),
    path('del_tiro_arma/<int:id>', views.del_tiro_arma, name='del_tiro_arma'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
