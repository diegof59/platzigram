from django import forms
# from .models import Profile
"""
class UpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['web_site', 'bio', 'birth_date', 'phone', 'profile_picture',]
"""
class ProfileForm(forms.Form):

	web_site = forms.CharField(max_length=200, required=True)
	bio = forms.CharField(max_length=500, required=False)
	phone = forms.CharField(max_length=20, required=False)
	profile_picture = forms.ImageField()