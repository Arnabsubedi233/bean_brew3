from django import forms
from .models import reservation

class ReserveTableForm(forms.ModelForm):
    class meta:
        model = reservation
        fields = '__all__'