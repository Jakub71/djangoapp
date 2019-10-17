from django.shortcuts import render
from django.http import HttpResponse

from studenci.models import Miasto, Uczelnia



def index(request):
    return HttpResponse("<h1>Witaj w aplikacji Studenci!</h1>")
    # return render(request, 'studenci/index.html')

def komunikat(request):
    return HttpResponse("<h1>Komunikat!</h1>")
    # return render(request, 'pizza/komunikat.html'

def miasta(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        kod = request.POST.get('kod', '')
        m = Miasto(nazwa=nazwa, kod=kod)
        m.save()

    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta}
    return render(request, 'studenci/miasta.html', kontekst)

def uczelnie(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        n = Uczelnia(nazwa=nazwa, )
        n.save()

    uczelnie = Uczelnia.objects.all()
    kontekst = {'uczelnie': uczelnie}
    return render(request, 'studenci/uczelnie.html', kontekst)