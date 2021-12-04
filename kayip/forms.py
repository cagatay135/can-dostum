from django import forms

class Form(forms.Form):
    your_name = forms.CharField(label='Adı', max_length=100)