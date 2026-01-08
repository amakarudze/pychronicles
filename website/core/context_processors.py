from datetime import datetime

import requests

from django.conf import settings


def footer_context(request):
    copyright_year = datetime.today().year
    return {"copyright_year": copyright_year}


def tags_context(request):
    tags = []
    try:
        tags_response = requests.get(
            f"{settings.BLOG_API}/api/blog/tags/",
            timeout=5,
        )
        if tags_response.ok:
            tags = tags_response.json()
    except requests.RequestException:
        return {"tags": tags}
    
    if tags:
        midpoint = len(tags) // 2
        return  {
            "tags_col1": tags[:midpoint],
            "tags_col2": tags[midpoint:],
        }
    else: 
        return {"tags": tags}
    