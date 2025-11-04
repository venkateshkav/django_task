from django.urls import path
from .views import *


app_name = 'survey'

urlpatterns = [
    path('home/',register_form,name="home"),
    path('details/',survey, name='survey'),
    path('thank-you/',thankyou, name='thankyou'),
    path('clear/',clear_session, name='clear_session'),
]

