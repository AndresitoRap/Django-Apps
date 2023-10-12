from django import forms
from .models import Coment

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ("coment", "author")