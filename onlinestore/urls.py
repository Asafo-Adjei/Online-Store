from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include('storeapp.urls')),
    path('items/', include('item.urls')), #This is the path for the urls.py file created in the "item" app folder
    path('admin/', admin.site.urls),
    path('inbox/', include('conversation.urls')),
    path('dashboard/', include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #this is not advised in production purposes

