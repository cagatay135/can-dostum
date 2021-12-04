from django import forms 
from .models import Comments 
  
class Comments(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Comments 
        fields = ['text']
        labels= {'text' : 'Yorumunuz'}