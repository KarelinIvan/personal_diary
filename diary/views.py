from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from diary.models import Post


class PostCreateView(CreateView):
    """ Создание статьи в дневнике """
    model = Post
    fields = ('title', 'image', 'content', 'author', 'created_at')


class PostListView(ListView):
    """ Просмотр всех статей """
    model = Post

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'diary/index.html', context={'posts': posts})


class PostDetailView(DetailView):
    """ Просмотр статьи """
    model = Post


class PostUpdateView(UpdateView):
    """ Изменение статьи """
    model = Post
    fields = ('title', 'image', 'content', 'author', 'created_at')


class PostDeleteView(DeleteView):
    """ Удаление статьи """
    model = Post
