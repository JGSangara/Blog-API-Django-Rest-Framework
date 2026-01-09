from django.utils.text import slugify
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "slug",
        )
        read_only_fields = ("slug",)

    def generate_unique_slug(self, title):
        slug = slugify(title)
        unique_slug = slug
        counter = 1

        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{counter}"
            counter += 1

        return unique_slug

    def create(self, validated_data):
        validated_data["slug"] = self.generate_unique_slug(
            validated_data["title"])
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if "title" in validated_data:
            if validated_data["title"] != instance.title:
                validated_data["slug"] = self.generate_unique_slug(
                    validated_data["title"]
                )
        return super().update(instance, validated_data)