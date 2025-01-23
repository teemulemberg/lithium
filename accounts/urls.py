from django.urls import path
from .views import UserSettingsView, UserProfileView

app_name = 'accounts'  # Add namespace

urlpatterns = [
    path('settings/', UserSettingsView.as_view(), name='user_settings'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
] 