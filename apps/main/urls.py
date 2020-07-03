from django.urls import path
from .views import Home, Tramites


urlpatterns = [
    path('', Home, name='index'),
    path('tramites/', Tramites, name='tramites'),
]
