from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('bungie/', include('destinyapp.bungie.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
