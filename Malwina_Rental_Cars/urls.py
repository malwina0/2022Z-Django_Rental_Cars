"""Malwina_Rental_Cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rental_app.views import (
    home,
    cars_list,
    car_retrieve,
    car_update,
    car_delete,
    rent_a_car,
    contact,
    calculate_cost
)
from Malwina_Rental_Cars import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('cars', cars_list),
    path('cars/<pk>/', car_retrieve),
    path('cars/<pk>/edit/', car_update),
    path('cars/<pk>/delete/', car_delete),
    path('', include('users.urls')),
    path('rent/', rent_a_car),
    path('contact', contact),
    path('price/', calculate_cost),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)