from django.urls import path
from .views import *

app_name = 'excursions'

urlpatterns = [
    path('', home, name='home'),
]
