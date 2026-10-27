from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import CommentForm, PostForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = ['-date']


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


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


def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # cria o comentário sem salvar ainda
            comment.post = post                # liga o comentário ao post
            comment.save()
            return HttpResponseRedirect(reverse('posts:detail', args=(post.id, )))
    else:
        form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'posts/comment.html', context)