from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/', include('apps.admin.urls')),
    path('api/client/', include('apps.client.urls')),
]