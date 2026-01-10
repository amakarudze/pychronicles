
import requests

from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, render

from django.views.generic import TemplateView

from .blog_api import fetch_blog_posts, fetch_blog_post
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = "core/index.html"


class AboutPageView(TemplateView):
    template_name = "core/about.html"


class BlogPageView(TemplateView):
    template_name = "core/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        search = self.request.GET.get("search")
        tag = self.request.GET.get("tag")

        try:
            if search or tag:
                data = fetch_blog_posts(search, tag)
            else:
                response = requests.get(
                    f"{settings.BLOG_API}/posts/",
                    timeout=5,
                )
                response.raise_for_status()
                data = response.json()

        except requests.RequestException:
            context["posts"] = []
            context["featured_post"] = None
            context["error"] = "Blog service unavailable"
            return context

        # Handle paginated or plain list responses
        if isinstance(data, dict):
            posts = data.get("results", [])
        else:
            posts = data
         
        if not search:
            if posts:
                context["featured_post"] = posts[0]
                context["posts"] = posts[1:]
        else:
            context["featured_post"] = None
            context["posts"] = posts

        context["search_query"] = search
        context["active_tag"] = tag

        return context


class BlogDetailView(TemplateView):
    template_name = "core/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]

        post = fetch_blog_post(slug)
        context["post"] = post

        tag = post["tags"][0] if post.get("tags") else None

        if tag:
            related = fetch_blog_posts(tag=tag)
            # Exclude the current post
            related = [p for p in related if p.get("slug") != slug]
        else:
            related = []

        context["related_posts"] = related

        return context


class ContactPageView(TemplateView):
    template_name = "core/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.send_email()
            messages.success(request, "Your message has been sent.")
            return redirect(reverse("contact"))

        return render(request, self.template_name, {"form": form})

