from django import forms
from .models import Tovar, Zakaz

class TovarForms(forms.ModelForm):
  class Meta:
    model = Tovar
    execude = ['id']

    widgets = {
      'nazvanie': forms.TextInput(attrs={'class': 'form_input'})
    }

class ZakazForms(forms.ModelForm):
  class Meta:
    model = Zakaz

    field = ['tovar', 'status', 'punktVidachi']

class FilterForm(forms.Form):
  q = forms.CharField(required=False, label='Поиск по названию')
  sort = forms.ChoiceField(required=False, choices=[
    {
      'nazvanie':'По названию'
    }
  ])