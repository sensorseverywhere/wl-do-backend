from urllib import response

from rest_framework import serializers
from accounts.serializers import UserAccountSerializer

from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    # filter for contentype tag == page
    author = UserAccountSerializer()
    class Meta:
        model = Content
        fields = ('id', 'author', 'type', 'title', 'active', 'content')
        depth = 1


    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     for author in response.get("author"):
    #         author.pop("password", None)
    #     return response