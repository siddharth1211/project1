from django import forms
from .models import document, apiData


class apidocForm(forms.ModelForm):
    class Meta:
        model = document
        fields = ('file',)
        widgets = {'file': forms.FileInput(attrs={'class': 'form-control', 'id': 'id_api_input'})}