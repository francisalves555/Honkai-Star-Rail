from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from .views import home_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', include('cadastro.urls')),
    path('tiro/', include('tiro.urls')),
    path('editar/', include('editar.urls')),
    path('home/', include('home.urls')),
    path('', home_redirect),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
