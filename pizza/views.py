from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from pizza.models import Pizza, Skladnik


def index(request):
    return HttpResponse("<h1>Witaj w aplikacji Pizza!</h1>")
    # return django.shortcuts.render(request, 'pizza/index.html')


def komunikat(request):
    return HttpResponse("<h1>Komunikat!</h1>")
    # return django.shortcuts.render(request, 'pizza/komunikat.html')


def pizza(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        opis = request.POST.get('opis', '')
        rozmiar = request.POST.get('rozmiar', '')
        cena = request.POST.get('cena', '')
        data = request.POST.get('data', '')
        if len(nazwa.strip()) and len(opis.strip()) and len(rozmiar.strip()) and len(cena.strip()) and len(
                data.strip()):
            m = Pizza(nazwa=nazwa, opis=opis, rozmiar=rozmiar, cena=cena, data=data)
            m.save()
            messages.success(request, "Dobrze!!!")
        else:
            messages.error(request, "Ło ty oszukisto skubany!!!")

    pizza = Pizza.objects.all()
    kontekst = {'pizza': pizza}
    return render(request, 'pizza/pizza.html', kontekst)
