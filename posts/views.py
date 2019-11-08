from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from posts.forms import PostForm

from .models import Post

# now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

class PostsFeedView(LoginRequiredMixin, ListView):
    
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 5
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):

    template_name = 'posts/details.html'
    query_set = Post.objects.all()
    context_object_name = 'post'

@login_required
def create_post(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(request, 'posts/create.html',
                  {'user': user, 'profile': profile, 'form': form})
