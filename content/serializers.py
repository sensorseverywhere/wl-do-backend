from rest_framework import serializers

from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    # filter for contentype tag == page

    class Meta:
        model = Content
        fields = ('id', 'author', 'type', 'title', 'active', 'content')
        depth = 1
