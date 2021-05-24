# from django.contrib.auth import models
# from django.contrib.auth import models
from django.shortcuts import render
from django.views.generic import DetailView
from . import models


class UserProfileView(DetailView):
    
    model = models.User
    context_object_name = "user_obj"
