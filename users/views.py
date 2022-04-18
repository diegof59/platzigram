from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView
from django.views.generic.edit import UpdateView
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy

from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

from .forms import ProfileForm, SignupForm


class SignupView(FormView):
    """View sign up"""
    
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    """View login"""
                
    template_name = 'users/login.html'


@login_required
def logout_view(request):
    """View logout"""
    logout(request)
    return redirect('users:login')


class UpdateProfileView(LoginRequiredMixin, FormView):
    """View para actualizar datos del perfil"""

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
    """View para detalles del usuario."""
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