from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt

from .models import Content
from .serializers import PageSerializer


class PageListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Content.objects.all()    
    serializer_class = PageSerializer


class PageAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PageSerializer


    def get(self, request, string):
        content = Content.objects.get(title=string)
        response = {
            "title": content.title,
            "content": content.content,
            "active": content.active,
            "tags": content.tags
        }
        return Response(response)


class PageCreateAPIView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = PageSerializer


class PageUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = PageSerializer


class DeleteContentAPIView(APIView):
    permission_classes = [IsAdminUser]
    @csrf_exempt
    def delete(self, request, pk):
        content = Content.objects.get(id=pk)
        content.delete()
        serializer_class = PageSerializer
        return Response('content deleted')
