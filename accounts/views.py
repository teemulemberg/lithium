from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import UserSettings, CustomUser
from .forms import UserSettingsForm, UserProfileForm

# Create your views here.

class UserSettingsView(LoginRequiredMixin, UpdateView):
    model = UserSettings
    form_class = UserSettingsForm
    template_name = 'account/settings.html'
    success_url = reverse_lazy('accounts:user_settings')

    def get_object(self, queryset=None):
        # Get or create settings for the current user
        settings, created = UserSettings.objects.get_or_create(user=self.request.user)
        return settings

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'API key saved successfully!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to save API key. Please try again.')
        return super().form_invalid(form)

class UserProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('accounts:user_profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)
