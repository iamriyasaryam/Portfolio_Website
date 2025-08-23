from django import forms
from .models import ContactModel

class EmailForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'message', 'email']