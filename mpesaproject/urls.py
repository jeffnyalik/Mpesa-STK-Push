from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('mpesa_api/', include('mpesa_api.urls')),
    path('api/v1/', include('mpesa_api.urls')),
    path('admin/', admin.site.urls),
]
