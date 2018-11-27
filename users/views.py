from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.urls import reverse

from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

from .forms import ProfileForm, SignupForm


# View sign up
def signup_view(request):
    
    if request.method == 'POST':
        
        form = SignupForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            redirect('users:login')

    else:
        form = SignupForm()
    
    return render(request, 'users/signup.html', {'form': form})

# View login
def login_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html',
                    {'error': 'Invalid username or password'}
                )
    return render(request, 'users/login.html')


# View logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


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
            
            profile_url = reverse('users:detail', kwargs={'username': user.username})
            return redirect(profile_url)
    else:
        form = ProfileForm()

    return render(request, 'users/update_profile.html',
                  {'user': user, 'profile': profile, 'form': form})
                  
class UserDetailView(LoginRequiredMixin, DetailView):
    
    template_name = 'users/details.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        
        return context