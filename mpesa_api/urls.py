from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('lipa/online', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
]
