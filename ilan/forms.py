from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True , label="İsminizi Giriniz")
    from_email = forms.EmailField(required=True , label="Mail")
    subject = forms.CharField(required=True , label="Konu Nedir?")
    message = forms.CharField(widget=forms.Textarea , label="Mesaj")

