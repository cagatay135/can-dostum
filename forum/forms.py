from django import forms 
from .models import ForumComments 
from .models import ForumPost 

class Posts(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = ForumPost 
        fields = ['title' , 'text' , 'tag']
        labels = {
            "title": "Başlık",
            "text" : "Yazı",
            "tag"  : "Etiket"
        }

class Comments(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = ForumComments 
        fields = ['text']
        labels = { 'text' : 'Yorumunuz'}