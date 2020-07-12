from django.urls import path
from .views import Home, Tramites, Contacto

app_name='main'

urlpatterns = [
    path('', Home, name='index'),
    path('tramites/', Tramites, name='tramites'),
    path('contacto/', Contacto, name='contacto'),
]
