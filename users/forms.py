from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile

"""
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['web_site', 'bio', 'birth_date', 'phone', 'profile_picture',]
"""

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirm = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}))
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirm = data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirm')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class ProfileForm(forms.Form):
    
    web_site = forms.CharField(max_length=200, required=True)
    bio = forms.CharField(max_length=500, required=False)
    phone = forms.CharField(max_length=20, required=False)
    profile_picture = forms.ImageField()
