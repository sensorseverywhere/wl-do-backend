
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import UserAccount


# @csrf_exempt
class CheckEmail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        email = request.GET.get('email')
        user = UserAccount.objects.filter(email=email)
        if user:
            print('Email exists')
            return Response('Email exists')
        else:
            print('Welcome aboard')
            return Response('Welcome aboard!')

