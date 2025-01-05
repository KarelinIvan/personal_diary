from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from diary.forms import PostForm
from diary.models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """ Создание статьи в дневнике """
    model = Post
    form_class = PostForm
    template_name = 'diary/post_create.html'
    success_url = reverse_lazy('diary:list_posts')

    def form_valid(self, form):
        """ Сохраняет объект модели, установив автора записи """
        post = form.save(commit=False)
        post.author = self.request.user  # Присваиваем текущему пользователю
        post.save()
        return super().form_valid(form)


class PostListView(LoginRequiredMixin, ListView):
    """ Просмотр всех статей """
    model = Post
    template_name = 'diary/index.html'
    context_object_name = 'posts'
    paginate_by = 5  # Укажите количество записей на странице


class PostDetailView(LoginRequiredMixin, DetailView):
    """ Просмотр статьи """
    model = Post
    template_name = 'diary/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """ Изменение статьи """
    model = Post
    fields = ('title', 'image', 'content', 'author', 'created_at')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """ Удаление статьи """
    model = Post
    template_name = 'diary/post_delete.html'
    success_url = reverse_lazy('diary:list_posts')
