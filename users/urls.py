from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = "register"),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('profile/<username>', views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('passord_change', views.password_change, name = 'password_change'),
    path('password_reset', views.password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>', views.password_reset_confirm, name='password_reset_confirm'),
]
