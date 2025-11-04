from django.urls import path
from .views import *


app_name = 'survey'
app_name = 'loginapp'


urlpatterns = [
    path('home/',register_form,name="home"),
    path('details/',survey, name='survey'),
    path('thank-you/',thankyou, name='thankyou'),
    path('clear/',clear_session, name='clear_session'),
    path('', login_view, name='login_view'),
    path('welcome/', welcome, name='welcome'),
    path('logout/', logout_view, name='logout'),
]



