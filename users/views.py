from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


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