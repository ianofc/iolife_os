from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from flow.views import flow_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', flow_home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)