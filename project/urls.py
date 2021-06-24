from django.urls import path
from .views import Userlogin, UserRegister, home, userLogout, userDelete


urlpatterns = [
    path('', Userlogin, name='login'),
    path('register/', UserRegister, name='register'),
    path('home/', home, name='home'),
    path('logout/', userLogout, name='logout'),
    path('delete/', userDelete, name='delete')
]