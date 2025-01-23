from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserSettings

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)

class UserSettingsForm(forms.ModelForm):
    openai_api_key = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500',
            'placeholder': 'sk-...',
            'autocomplete': 'off'  # Prevent browser from saving API key
        }),
        required=False,
        help_text="Enter your OpenAI API key"
    )

    class Meta:
        model = UserSettings
        fields = ['openai_api_key']

    def clean_openai_api_key(self):
        key = self.cleaned_data.get('openai_api_key')
        if key and not key.startswith('sk-'):
            # Just a basic check to ensure it starts with sk-
            raise forms.ValidationError("API key should start with 'sk-'")
        return key

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'bio', 'address', 'phone', 'company', 'position']
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 4,
                'class': 'mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500'
            }),
            'address': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500'
            }),
            'company': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500'
            }),
            'position': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500'
            }),
        }