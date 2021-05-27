from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('user/', include('members.urls')),
    path('group/', include('circle.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # статик файлдарды қосу 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
