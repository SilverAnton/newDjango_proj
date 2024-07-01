from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogDeleteView, BlogUpdateView, BlogDetailView, BlogListView

app_name = BlogConfig.name
urlpatterns = [
    path("blog/", BlogCreateView.as_view(), name="blog_create"),
    path("blog_list/blog/", BlogListView.as_view(), name="blog_list"),
    path("blog_detail/blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("edit/blog/<int:pk>/", BlogUpdateView.as_view(), name="blog_edit"),
    path("delete/blog/<int:pk>/",BlogDeleteView.as_view(), name="blog_delete"),

]