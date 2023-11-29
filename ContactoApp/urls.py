from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto, name='Contacto'),
    path('contacto/<valido>', views.contacto, name='valido'),
    path('contacto/<invalido>', views.contacto, name='invalido'),
]
