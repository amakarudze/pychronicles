import requests
from django.conf import settings


def fetch_blog_posts(search=None, tag=None):
    params = {}
    if search:
        params["search"] = search
    if tag:
        params["tag"] = tag

    response = requests.get(
        f"{settings.BLOG_API}/posts/",
        params=params,
        timeout=5,
    )
    response.raise_for_status()
    return response.json()  # always LIST


def fetch_blog_post(slug):
    response = requests.get(
        f"{settings.BLOG_API}/posts/{slug}/",
        timeout=5,
    )
    response.raise_for_status()
    return response.json()  # always OBJECT
