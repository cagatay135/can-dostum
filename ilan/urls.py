from django.contrib import admin
from django.urls import path

from .views import HomePage , AboutPage , CovidPage , ContactPage , SignUpView

urlpatterns = [
    path('' , HomePage , name = 'home'),
    path('hakkimizda/' , AboutPage , name = 'about'),
    path('covid19/' , CovidPage.as_view() , name = 'covid19'),
    path('iletisim/' , ContactPage , name = 'contact'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
