from django.urls import path
from . import views
from django.views.generic import ListView
from studenci.models import Miasto, Uczelnia

app_name = 'studenci'
urlpatterns = [
    path('', views.index, name='index'),
    path('miasta/', ListView.as_view(model=Miasto,context_object_name='miasta',template_name='studenci/lista_miast.html'), name='miasta_lista'),
    path('miasta/dodaj', views.miasta, name='miasta_dodaj'),
    path('uczelnie/lista', ListView.as_view(model=Uczelnia,context_object_name='uczelnie',template_name='studenci/lista_uczelnie.html'), name='uczelnia_lista'),
    path('uczelnie/', views.uczelnie, name='uczelnie'),
    path('login/', views.loguj_studenta, name='login'),
]