import pytest
from django.test import Client
from wagtail.models import Site, Page, Locale

from core.models import HomePage


@pytest.fixture
def client(db):
    """Enable db access"""
    client = Client()
    return client


@pytest.fixture
def wagtail_tree(db):
    """
    Create the root page + home page needed for Wagtail routing.
    """
    locale, _ = Locale.objects.get_or_create(language_code="en")

    root = Page.add_root(
        title="Root",
        slug="root",
        locale=locale,
    )

    Site.objects.update_or_create(
        id=1,
        defaults={
            "hostname": "localhost",
            "root_page": root,
            "is_default_site": True,
        },
    )

    return root


@pytest.fixture
def blog_home(wagtail_tree):
    root = Page.objects.get(id=1)

    blog = HomePage(
        title="Blog",
        slug="blog",
    )
    
    root.add_child(instance=blog)
    blog.save_revision().publish()

    Site.objects.update_or_create(
        id=1,
        defaults={"hostname": "localhost", "root_page": root},
    )

    return blog