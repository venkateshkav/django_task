from django.urls import path
from .views import *

urlpatterns = [
    path('home/',register_form,name="home"),
    path('details/',show_details,name="detail"),
]