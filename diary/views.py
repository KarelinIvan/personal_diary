from django.shortcuts import render
from django.core.paginator import Paginator
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
        # Выводи статьи в порядке их создания/редактирования
        posts = Post.objects.all().order_by('-created_at')
        # Делаем вывод 5 статей на страницу
        paginator = Paginator(posts, 5)

        # сохраняем из запроса номер страницы на которой находится пользователь
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'diary/index.html', context={'page_obj': page_obj})


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
