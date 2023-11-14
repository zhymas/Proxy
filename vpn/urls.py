from django.urls import path
from .views import home, create_proxy, last_vpn_connection

urlpatterns = [
    path('', home, name='home'),
    path('proxy/', create_proxy, name='create_proxy'),
    path('history_proxy/', last_vpn_connection, name='history_connect')

]
