from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from newapp.views import index  # Updated Import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
