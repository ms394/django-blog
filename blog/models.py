from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model



class Comment(models.Model):
    article = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=150)
    author  = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[str(self.id)])



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='postImages', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
