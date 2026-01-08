from rest_framework import serializers

from .models import BlogPage


class BlogPageSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = BlogPage
        fields = ["date","title", "text", "intro", "author", "slug", "tags"]

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]
