from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.BlogListAPIView.as_view(), name="api_blog_list"),
    path("posts/<slug:slug>/", views.BlogDetailAPIView.as_view(), name="api_blog_detail"),
    path("tags/", views.TagListAPIView.as_view(), name="api_tag_list"),
]
