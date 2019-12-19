from django.forms import ModelForm, ModelMultipleChoiceField, Textarea

from pizza.models import Pizza, Skladnik

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        exclude = ('data',)


class SkladnikForm(ModelForm):
    class Meta:
        model = Skladnik
        fields = ('nazwa', 'jarski')