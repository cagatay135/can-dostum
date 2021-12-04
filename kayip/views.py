from django.shortcuts import render
from . forms import  Form

# Create your views here.
def AddLostPet(request):
    if request.method == 'GET':
        form = Form()
    else:
        form = Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']            
    return render(request, "add_lost.html", {'form': form})