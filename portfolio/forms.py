from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
