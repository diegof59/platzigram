from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy

from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

from .forms import ProfileForm, SignupForm


# View sign up
class SignupView(FormView):
    
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

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
class UpdateProfileView(LoginRequiredMixin, FormView):

    form_class = ProfileForm
    template_name = 'users/update_profile.html'

    def form_valid(self, form):
        
        user = self.request.user
        profile = user.profile

        form.save(profile)

        return super().form_valid(form)

    def get_success_url(self):
        usrname = self.request.user.username
        url = reverse_lazy('users:details', kwargs={'username': usrname})
        return url
                  
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