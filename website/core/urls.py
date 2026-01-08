from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("blog/", views.BlogPageView.as_view(), name="blog"),
    path("blog/post_detail/<slug:slug>/", views.BlogDetailView.as_view(), name="post_detail"),
    path("contact/", views.ContactPageView.as_view(), name="contact"),
]
