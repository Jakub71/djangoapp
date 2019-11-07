from django import forms

class UserLoginForm(forms.Form):
    login = forms.CharField(label="Twój login", max_length=20, widget=forms.TextInput())

class UczelniaForm(forms.Form):
    nazwa = forms.CharField(label="twoja szkoła", max_length=50, widget=forms.TextInput())

class MiastaForm(forms.Form):
    nazwa = forms.CharField(label="Podaj miasto", max_length=50, widget=forms.TextInput())
    kod = forms.CharField(label="Podaj kod", max_length=10, widget=forms.TextInput())