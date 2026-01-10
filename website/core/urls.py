from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("blog_posts/", views.BlogPageView.as_view(), name="blog_posts"),
    path("post_detail/<slug:slug>/", views.BlogDetailView.as_view(), name="post_detail"),
    path("contact/", views.ContactPageView.as_view(), name="contact"),
]
