from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

from studenci.models import Miasto, Uczelnia
from studenci.forms import UserLoginForm, UczelniaForm, MiastaForm


def index(request):
    # return HttpResponse("<h1>Witaj wsród sudentów!</h1>")
    return render(request, 'studenci/index.html')

def komunikat(request):
    return HttpResponse("<h1>Komunikat!</h1>")
    # return render(request, 'pizza/komunikat.html'

def miasta(request):
    if request.method == 'POST':
        #nazwa = request.POST.get('nazwa', '')
        #kod = request.POST.get('kod', '')
        #if len(nazwa.strip()) and len(kod.strip()):
        form = MiastaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            m = Miasto(nazwa=form.cleaned_data['nazwa'], kod=form.cleaned_data['kod'])
            m.save()
            messages.success(request, "Dobrze!!!")
            return redirect(reverse('studenci:miasta'))
        else:
            messages.error(request, "Ło ty oszukisto!!!")
    else:
        form = MiastaForm()
    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta, 'form': form}
    return render(request, 'studenci/miasta.html', kontekst)

def uczelnie(request):
    if request.method == 'POST':
        form = UczelniaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u = Uczelnia(nazwa=form.cleaned_data['nazwa'])
            u.save()
            messages.success(request, "Dobrze!!!")
            return redirect(reverse('studenci:uczelnie'))
        else:
            messages.error(request, "Ło ty oszukisto!!!")

    else:
        form = UczelniaForm()
    uczelnie = Uczelnia.objects.all()
    kontekst = {'uczelnie': uczelnie, 'form': form}
    if request.user.has_perm('studenci.add_uczelnia'):
     return render(request, 'studenci/uczelnie.html', kontekst)
    else:
        messages.info(request, "Nie możesz dodawać uczelni")
        return redirect(reverse('studenci:index'))

def loguj_studenta(request):
    if request.method == 'POST':
        pass
    else:
        form = UserLoginForm()
    kontekst = {'form': form}
    return render(request, 'studenci/login.html', kontekst)

