"""
URL configuration for MusicProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', category_page),
    re_path(r'^main', main_page),
    re_path(r'^rock', rock_page, name='rock'),
    re_path(r'^hip-hop', hip_hop_page, name='hip-hop'),
    re_path(r'^pop', pop_page, name='pop'),
    re_path(r'^jazz', jazz_page, name='jazz'),
    re_path(r'^electronic', electronic_page, name='electronic'),
    re_path(r'^linkinPark', linkin_park_page, name='linkin'),
    # re_path(r'^queen', queen_page, name='queen'),
    # path('<slug:product_slug>/', queen_page, name='product_detail'),
    path('artist/<slug:product_slug>/', queen_page, name='artist_detail'),
    re_path(r'^systemOfDown', system_of_down_page, name='system'),
    re_path(r'^2pac', two_pac_page, name='2pac'),
    re_path(r'^kendrick_lamar', kendrick_lamar_page, name='kendrick'),
    re_path(r'^eminem', eminem_page, name='eminem'),
    re_path(r'^adele', adele_page, name='adele'),
    re_path(r'rihanna', rihanna_page, name='rihanna'),
    re_path(r'beyonce', beyonce_page, name='beyonce'),
    re_path(r'frank_sinatra', frank_sinatra_page, name='frank_sinatra'),
    re_path(r'ray_charles', ray_charles_page, name='ray_charles'),
    re_path(r'louis_armstrong', louis_armstrong_page, name='louis_armstrong'),
    re_path(r'avicii', avicii_page, name='avicii'),
    re_path(r'daft_punk', daft_punk_page, name='daft_punk'),
    re_path(r'moby', moby_page, name='moby'),

]
