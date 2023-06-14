from django.contrib import admin
from django.urls import path, include
from .views import register_view, login_view, index, profile_view, oikawakuroo

urlpatterns = [
    path('home/', index, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('oikawakuroo/',oikawakuroo, name = 'oikawakuroo' )
]
