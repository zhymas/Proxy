from django.urls import path
from .views import UserCreate, logout_user, UserAuth, user_account

urlpatterns = [
    path('create/', UserCreate.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', UserAuth.as_view(), name='auth'),
    path('user_account/', user_account, name='user_account'),

]