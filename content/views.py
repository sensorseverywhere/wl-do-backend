from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Content, Story
from accounts.models import UserAccount
from .serializers import ContentSerializer

from .forms import StoryFormSet, StoryForm


class ContentListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Content.objects.all()    
    serializer_class = ContentSerializer


class ContentDetailAPIView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = ContentSerializer

    def get(self, request, pk):
        content = Content.objects.get(id=pk)
        response = {
            "title": content.title,
            "content": content.content,
            "active": content.active,
            "type": content.type,
            "author": content.author
        }
        return Response(response)


class GetContentTypesAPIView(APIView):
    permission_class = [IsAdminUser]
    serializer_class = ContentSerializer
    # model = Content

    def get(self, request):
        types = Content._meta.get_field('type').choices
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


def create_story(request, pk):
    author = UserAccount.objects.get(id=pk)
    stories = Story.objects.filter(author=author)
    form = StoryForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            story = form.save(commit=False)
            story.author = author
            story.save()
            return redirect("story-detail", pk=story.id)
        else: 
            return render(request, "stories/create_story.html", context={"form": form})

    context = {
        "form": form,
        "author": author,
        "stories": stories
    }

    return render(request, "create_story.html", context)


def create_story_form(request):
    form = StoryForm()
    context = {
        "form": form
    }
    return render(request, "stories/story_form.html", context)


def detail_story(request, pk):
    story = get_object_or_404(Story, id=pk)
    context = {
        "story": story
    }
    return render(request, "stories/story_detail.html", context)


def update_story(request, pk):
    story = Story.objects.get(id=pk)
    form = StoryForm(request.POST or None, instance=story)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("stories/story_detail.html", pk=story.id)

    context = {
        "form": form,
        "story": story
    }

    return render(request, "stories/story_form.html", context)    


def delete_story(request, pk):
    story = get_object_or_404(Story, id=pk)

    if request.method == "POST":
        story.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
