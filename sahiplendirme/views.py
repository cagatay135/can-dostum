from django.shortcuts import render, redirect
from . forms import  AddPetForm
from django.contrib.auth.decorators import login_required
import firebase_admin
from firebase_admin import credentials, firestore , storage
from django.urls import reverse

config = {
  "type": "service_account",
  "project_id": "fire-e4727",
  "private_key_id": "05f4868f9ea8c46a2bf4032ddabfc288918d7e3d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCkKH3PRIEousKV\napq3vWvzUmpcq2SINcRg3viwd/iUD4zDDxTEgOeOxcS9MpdniG4L/wOgTtH3JQoe\nEJfZbx4+hCA82UqZ59rQxAvaefz8PrJz+OyPDJJaGh/Lma65+SAQVBDnNWjXSNjt\nJ9Bt4mKKKfQCim2vqwaCkqpyMC6JVUEnSI+WvF0KGhxmT/kVNjjZsaDu6m7LLD5W\nMy199fPuUJPu/thYo8yfRgTZyGUG70mWdKR7otRNCQGPUyAsyAZ0GHugSa2v9Hpy\np3Nv/nAxt/EtDJLeb6e6dsty1i37x/q2kKMsIdXaDeFP/XIAwFyCERd1ErKrsKEO\nlO1TkGEJAgMBAAECggEAQtapwwalgCvqpmOtczqRBZV88RZn7H3X44llwJRYhhB+\nw70UO54wqhUkMdSziNgn1oKSu2bcXsCaCfu/mCyCJ/osFhpzIY8hrPblzKL2us3c\nYxPrXaNEw6L3ZzK/zcD9qShRaZJ5iY6DpKwdVWBjttW2IIK0fl4oXGnTNIMhr5B7\n1L2DhdHo8xitl+g0y3Vox9FL3wNgZaZjyBTXwjBGCUJiVAb86Ez2SogyKUurncOb\n6RWKQCBtoU/Sf4sLC3tj1QSVVFN5cS/sWISap58DCJw680Lq77oBlQEGWfc4Xy3j\nAml/4IKQcR350YmHsl5TiEc+i+tpddxhWs9naP2I8QKBgQDU2Qo6M/Zcq5VweqWs\n9QIHVrd8tjm9zTRFQU0kSVxSYg5u9OiuzuEceTSsbCjuuWMd/lrR1A8BhPsfwGfS\nWHYb/+0lelOCXmhRZeL9TMaBKdvsBLv+LlvP2PdGrsbI9YT1cLvwNHcTdRL+mYi1\ndjw1gNVpXp9FykpQzcgi41XWwwKBgQDFcGw6QtTnG9hcZt7Jp2DIbdACN9ppJOSA\nyl5EPFAt1RcXchxyYXy0muVcZ6g9w0BTOpr2GN+PEjgig8QZJ5IMEQEQJLnToAy9\njp6X3flRiwhPJkNSAUUkhnxgx50rBEhy6E5TeJVzuoh/8KOKztfA3SJJefBI1YYs\nHJEO0adkQwKBgBihhS13Fetjb8e0abe6IqH2xwUHkWcFeCcLh4HLe4ONFV6BuOuB\nxUsmO5I4cgQuL+oopRnjEFl8qhLikSEmW4Sh+S99GGzdv/SrdbkaSV5pGaoWYirn\n8nf7A6KKVzaqMti0UwtZBu6Zfbk4yzk0lYMbhZbL/GJ3JmJzbdWbuTNBAoGAPzL3\nUcbmw3uETD+ZfM8ZCc8s0Cj0vsdSZW9hsVHlEGavV4/tTyepdV5HoMaFcg+33Wxb\nAf+AQBnC4jlvYeXqt/YRcwtueDE5IswuM8qX7eQlKsDCt9M0QLbTxV7gDk72qeF2\ngP2OSVciLmHm153SLigau45OveGrax9Rx36QqGUCgYBodBkzdXxxv5ADzaIvtEUg\n4WWUQMO3usfUL1z+W/zTCxvSxm5uOU760GOBtNvyow/LmqKZvCeae0bSVNj/AI+1\nmioG+CqJudY6XKfJg2SEbnY95cen4eTYhkS3tQQihNDGTqqIDrB56nSnzJH224gH\n+c5O0CX2j3w9ZjbBWl1Ckg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-m9pum@fire-e4727.iam.gserviceaccount.com",
  "client_id": "104493439978389796008",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-m9pum%40fire-e4727.iam.gserviceaccount.com"
}

cred = credentials.Certificate(config)
firestore_db = firestore.client()

def PetsView(request):
    snapshots = list(firestore_db.collection(u'sahiplendirilecek_hayvanlar').stream())
    collections = []

    for snapshot in snapshots:
        dic = snapshot.to_dict()
        dic["id"] = snapshot.id
        book_data = {"collects": dic }
        collections.append(book_data)

    return render(request , 'pets.html' , {'snapshots' : collections})

@login_required(login_url='login')
def AddPet(request):
    if request.method == 'GET':
        form = AddPetForm()
    else:
        form = AddPetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            kind = form.cleaned_data['kind']
            age = form.cleaned_data['age']
            city = form.cleaned_data['city']
            sex = form.cleaned_data['sex']
            url = form.cleaned_data['url']
            
            firestore_db.collection(u'sahiplendirilecek_hayvanlar').add({'name': name , 'url' : url , 'age' : str(age) , 'sex' : sex , 'kind' : kind , 'description' : description , 'adress' : city})
            return redirect(reverse('sahiplendirme'))

            print(name , description , kind , age , city)
            
    return render(request, "add_pet.html", {'form': form})


def DetailView(request , id):
    snapshots = firestore_db.collection(u'sahiplendirilecek_hayvanlar').document(id).get()
    collections = []

    book_data = {"collects": snapshots.to_dict()}
    collections.append(book_data)

    return render(request , 'pets_detail.html' , {'animal' : collections})

def PetFilter(request , kind):
    snapshots = list(firestore_db.collection(u'sahiplendirilecek_hayvanlar').where(u'kind', u'==', kind).stream())
    collections = []
    
    for snapshot in snapshots:
        dic = snapshot.to_dict()
        dic["id"] = snapshot.id
        book_data = {"collects": dic }
        collections.append(book_data)

    return render(request , 'pet_filter.html' , {'animal' : collections})
