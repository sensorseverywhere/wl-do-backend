from email import contentmanager
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt

from .models import Content
from accounts.models import UserAccount
from .serializers import ContentSerializer


class ContentListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Content.objects.all()    
    serializer_class = ContentSerializer


class ContentAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ContentSerializer

    def get(self, request, string):
        content = Content.objects.get(title=string)
        response = {
            "title": content.title,
            "content": content.content,
            "active": content.active,
            "tags": content.tags
        }
        return Response(response)


class GetContentTypesAPIView(APIView):
    permission_class = [AllowAny]
    serializer_class = ContentSerializer
    # model = Content

    def get(self, request):
        types = Content._meta.get_field('type').choices
        print(types)
        return Response(types)


class ContentCreateAPIView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class UpdateContentAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, id):
        content = Content.objects.get(pk=id)
        author = UserAccount.objects.get(id=content.author)
        return content


    def patch(self, request, pk):
        content = self.get_object(id=pk)
        serializer = Content(content, data=request.data, partial=True)

        if serializer.is_valid():
           serializer.save()

           return Response(serializer.data) 
        return Response('Content updated')


class DeleteContentAPIView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        content = Content.objects.get(id=pk)
        content.delete()
        serializer_class = ContentSerializer
        return Response('content deleted')
