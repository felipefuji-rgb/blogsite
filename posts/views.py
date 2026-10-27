from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import PostForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = ['-date']


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'

    def get_success_url(self):
        return reverse('posts:detail', args=(self.object.id, ))


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'

    def get_success_url(self):
        return reverse('posts:detail', args=(self.object.id, ))


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:index')