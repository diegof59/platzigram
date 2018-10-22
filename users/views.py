from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from users.models import Profile

from .forms import ProfileForm

from django.db.utils import IntegrityError

# View sign up
def signup_view(request):

	if request.method == 'POST':
		
		username = request.POST['username']
		password = request.POST['password']
		password_confirm = request.POST['password_confirm']
		
		if password != password_confirm:
			return render(request, 'users/signup.html',
				{'error': 'Password and password confirmation differ.'})
		
		try:
			user = User.objects.create(username=username, password=password)
		except IntegrityError:
			return render(request, 'users/signup.html',
				{'error': 'Username is already in use.'})
				
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		
		user.first_name = first_name
		user.last_name = last_name
		user.email = email
		user.save()
		
		profile = Profile(user=user)
		profile.save()
		
		return render(request, 'users/login.html')
		
	return render(request, 'users/signup.html')

# View login 
def login_view(request):

	if request.method == 'POST':
		
		username = request.POST['username']
		password = request.POST['password']
		#print("POST ", username, ":", password)
		user = authenticate(request, username=username, password=password)
		
		if user:
			login(request, user)
			return redirect('feed')
		else:
			return render(request, 'users/login.html',
				{'error': 'Invalid username or password'}
				)
	return render(request, 'users/login.html')

# View logout
@login_required	
def logout_view(request):

	logout(request)
	return redirect('login')
	
# View para actualizar datos del perfil
@login_required
def update_profile(request):

	user = request.user
	profile = user.profile
	
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			
			data = form.cleaned_data
			
			profile.web_site = data['web_site']
			profile.bio = data['bio']
			profile.phone = data['phone']
			profile.profile_picture = data['profile_picture']
	
			profile.save()
			
			return redirect('feed')
	else:
		form = ProfileForm()
	
	return render(request, 'users/update_profile.html',
		{'user': user, 'profile': profile, 'form': form})