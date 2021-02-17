from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse



class HomePageView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'
    ordering = ['-created_date']


class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/bloglist.html'
    ordering = ['-created_date']

    def get_queryset(self):
        return Post.objects.order_by('-created_date')


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/blogdetail.html'


class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'body', 'image']
    template_name = 'blog/createblog.html'

    def form_valid(self,form):
        blog = form.save(commit=False)
        fs =  self.request.FILES
        print(fs)
        user = self.request.user
        blog.author = user
        form.save()
        return super(BlogCreateView, self).form_valid(form)



class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title','body', 'image']
    template_name = 'blog/blogupdate.html'



class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/blogdelete.html'
    success_url = reverse_lazy('blog:blog-list')
