'''

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import UserProfile
from .forms import UserProfileForm, UserForm
from lib.mixins import CheckObjectUserMixin

#might not need profile create view
class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = UserProfile
    form_class = UserProfileForm

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile

class ProfileUpdateView(LoginRequiredMixin, CheckObjectUserMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm

class ProfileDestroyView(LoginRequiredMixin, CheckObjectUserMixin, DeleteView):
    model = UserProfile


'''