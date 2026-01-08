from django.db.models import Q

from .models import BlogPage


def get_blog_queryset(params):
    queryset = BlogPage.objects.live().public()

    search = params.get("search")
    tag = params.get("tag")

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(text__icontains=search) |
            Q(intro__icontains=search)
        )

    if tag:
        queryset = queryset.filter(tags__name=tag)

    return queryset.distinct().order_by("-date")