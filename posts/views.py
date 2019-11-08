from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

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

class CreatePostView(LoginRequiredMixin, CreateView):

    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
