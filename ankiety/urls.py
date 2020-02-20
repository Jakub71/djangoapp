from django.urls import path
from . import views

app_name = 'ankiety'
urlpatterns = [
    path('', views.ListaPytan.as_view(), name='lista_pytan'),
    path('pytanie/glosuj/<int:pk>', views.pytanie_glosuj, name='pytanie-glosuj'),
]