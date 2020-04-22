from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin  # 追加

from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm
from .models import Post, Category

class IndexView(generic.ListView):
    template_name = 'blog/post_list.html'
    model = Post
    paginate_by = 10 # 追加

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset

class CategoryView(generic.ListView):
    template_name = 'blog/post_list.html'
    model = Post
    paginate_by = 10 # 追加

    def get_queryset(self):

        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        # queryset = Post.objects.order_by('created_at').filter(category=category)
        queryset = Post.objects.order_by('created_at').filter(category=category)
        return queryset


class DetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    
class AddView(LoginRequiredMixin, generic.CreateView):
    template_name = 'blog/post_form.html'
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:index')
    
class UpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'blog/post_form.html'
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:index')

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'blog/post_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('blog:index')