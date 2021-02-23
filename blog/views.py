from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class HomePageView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'
    ordering = ['-created_date']


class BlogListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/bloglist.html'
    ordering = ['-created_date']
    login_url = 'login'

    def get_queryset(self):
        return Post.objects.order_by('-created_date')


class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/blogdetail.html'
    login_url = 'login'


class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'body', 'image']
    template_name = 'blog/createblog.html'
    login_url = 'login'

    def form_valid(self,form):
        blog = form.save(commit=False)
        fs =  self.request.FILES
        print(fs)
        user = self.request.user
        blog.author = user
        form.save()
        return super(BlogCreateView, self).form_valid(form)



class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','body', 'image']
    template_name = 'blog/blogupdate.html'
    login_url = 'login'

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user



class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/blogdelete.html'
    success_url = reverse_lazy('blog:blog-list')
    login_url = 'login'

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user