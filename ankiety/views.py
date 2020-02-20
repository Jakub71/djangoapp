from django.shortcuts import render
from django.views.generic import ListView
from ankiety.models import Pytanie, Odpowiedz
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

class ListaPytan(ListView):
    model = Pytanie
    template_name = 'ankiety/lista_pytan.html'
    context_object_name = 'pytania'

    def get_queryset(self):
        return Pytanie.objects.order_by('-data_d')[:10]

@login_required()
def pytanie_glosuj(request, pid):
    pytanie = get_object_or_404(Pytanie, pk=pid)
    if request.method == 'POST':
        pass
    else:
        return render(request,'ankiety/pytanie_glosuj.html', {'pytanie':pytanie})