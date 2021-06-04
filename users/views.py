from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from . import models, forms


class UserProfileView(LoginRequiredMixin, DetailView):
    
    model = models.User
    context_object_name = "user_obj"


class UpdateProfileView(LoginRequiredMixin,UpdateView):

    model = models.User
    template_name = "users/update-profile.html"
    fields = (
        "first_name",
        "last_name",
        "avatar",
    )
    success_message = "Профиль обновлён."

    def get_object(self, queryset=None):
        return self.request.user

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["first_name"].widget.attrs = {"placeholder": "Имя", "class": "update-input"}
        form.fields["last_name"].widget.attrs = {"placeholder": "Фамилия", "class": "update-input"}
        return form
