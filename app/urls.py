from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('user/', include('users.urls', namespace="user")),
    path('cars/', include('cars.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),    
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # подключение MEDIA (фотографий) файлов к url адресу