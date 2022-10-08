from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ContentType
from .serializers import PageSerializer


class PageListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = ContentType.objects.all()    
    serializer_class = PageSerializer


class PageAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PageSerializer

    def get(self, request, string):

        content = ContentType.objects.get(title=string)

        response = {
            "title": content.title,
            "content": content.content,
            "active": content.active,
            "tags": content.tags
        }
        return Response(response)


class PageCreateAPIView(generics.ListCreateAPIView):
    queryset = ContentType.objects.all()
    serializer_class = PageSerializer


class PageUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = ContentType.objects.all()
    serializer_class = PageSerializer
