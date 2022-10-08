from rest_framework import serializers

from .models import ContentType


class PageSerializer(serializers.ModelSerializer):
    # filter for contentype tag == page

    class Meta:
        model = ContentType
        fields = ('id', 'tags', 'title', 'active', 'content')
