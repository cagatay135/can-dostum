from django import forms

GEEKS_CHOICES =( 
    ("Kedi", "Kedi"), 
    ("Köpek", "Köpek"), 
    ("Kuş", "Kuş"), 
    ("Hamster", "Hamster"), 
    ("Tavşan", "Tavşan"),
    ("Diğer", "Diğer"), 
) 

SEHIRLER =( 
    ("İstanbul", "İstanbul"), 
    ("Edirne", "Edirne"), 
    ("Ankara", "Ankara"), 
    ("İzmir", "İzmir"), 
    ("Antalya", "Antalya"), 
) 

YASI =( 
    ("0-3 Ay", "0-3 Ay"), 
    ("6-12 Ay", "6-12 Ay"), 
    ("1 Yaş", "1 Yaş"), 
    ("2 Yaş", "2 Yaş"), 
    ("3 Yaş", "3 Yaş"), 
    ("4 Yaş", "4 Yaş"), 
    ("5 + Yaş", "5 + Yaş"), 
) 

CINSIYET =( 
    ("Dişi", "Dişi"), 
    ("Erkek", "Erkek"), 
) 

class AddPetForm(forms.Form):
    name = forms.CharField(required=True , label="Can Dostumuzun İsmi")
    description = forms.CharField(label='Açıklama',
                           max_length=500,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))    
    kind = forms.ChoiceField(choices = GEEKS_CHOICES , label="Can Dostumuz") 
    sex = forms.ChoiceField(choices = CINSIYET , label="Cinsiyet") 

    age = forms.ChoiceField(required=True , choices = YASI , label="Yaşı")
    city = forms.ChoiceField(choices = SEHIRLER , label="Şehir") 
    url = forms.URLField(required=True , label="Resim URL")

