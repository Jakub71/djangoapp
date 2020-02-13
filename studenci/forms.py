from django import forms
from django.forms import ModelForm
from studenci.models import Uczelnia, Miasto

class UczelniaModelForm(ModelForm):
        class Meta:
            model = Uczelnia
            fields = ('nazwa',)


class MiastoModelForm(ModelForm):
    class Meta:
        model = Miasto
        fields = ('nazwa','kod',)

class UserLoginForm(forms.Form):
    login = forms.CharField(label="Twój login", max_length=20, widget=forms.TextInput())

class UczelniaForm(forms.Form):
    nazwa = forms.CharField(label="twoja szkoła", max_length=50, widget=forms.TextInput())

class MiastaForm(forms.Form):
    nazwa = forms.CharField(label="Podaj miasto", max_length=50, widget=forms.TextInput())
    kod = forms.CharField(label="Podaj kod", max_length=10, widget=forms.TextInput())

