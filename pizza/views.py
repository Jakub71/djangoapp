from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the jungle!</h1>")

def komunikat(request):
    return HttpResponse("<h2>Wstawaj samuraju!</h2>")

def apel(request):
    return HttpResponse("<h3>Padłeś?Powstań!</h3>")

