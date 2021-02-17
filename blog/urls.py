from django.urls import path
from  .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, HomePageView

app_name = 'blog'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blogs', BlogListView.as_view(), name='blog-list'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('createblog',BlogCreateView.as_view(),name='create-blog' ),
    path('updateblog/<int:pk>', BlogUpdateView.as_view(), name='blog-update'),
    path('deleteblog/<int:pk>', BlogDeleteView.as_view(), name='blog-delete')
]