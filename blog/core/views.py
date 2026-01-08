from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from taggit.models import Tag

from .models import BlogPage
from .serializers import BlogPageSerializer
from .utils import get_blog_queryset


class BlogListAPIView(APIView):
    def get(self, request):
        slug = request.query_params.get("slug")

        queryset = get_blog_queryset(request.query_params)

        if slug:
            page = get_object_or_404(queryset, slug=slug)
            serializer = BlogPageSerializer(page)
            return Response(serializer.data)

        serializer = BlogPageSerializer(queryset, many=True)
        return Response(serializer.data)


class BlogDetailAPIView(APIView):
    def get(self, request, slug):
        page = get_object_or_404(
            BlogPage.objects.live().public(),
            slug=slug
        )
        serializer = BlogPageSerializer(page)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagListAPIView(APIView):
    def get(self, request):
        tags = Tag.objects.all().order_by("name")
        return Response([tag.name for tag in tags])
