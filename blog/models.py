from django.db import models
from django.urls import reverse


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
