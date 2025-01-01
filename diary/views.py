from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from diary.models import Post
from django.urls import reverse_lazy


class PostCreateView(CreateView):
    """ Создание статьи в дневнике """
    model = Post
    fields = ('title', 'image', 'content', 'author', 'created_at')


class PostListView(ListView):
    """ Просмотр всех статей """
    model = Post
    template_name = 'diary/index.html'
    context_object_name = 'posts'
    paginate_by = 5  # Укажите количество записей на странице


class PostDetailView(DetailView):
    """ Просмотр статьи """
    model = Post
    template_name = 'diary/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    """ Изменение статьи """
    model = Post
    fields = ('title', 'image', 'content', 'author', 'created_at')


class PostDeleteView(DeleteView):
    """ Удаление статьи """
    model = Post
    template_name = 'diary/post_delete.html'
    success_url = reverse_lazy('diary:list_posts')
