from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from .models import UserAccount
from .serializers import UserAccountSerializer

# @csrf_exempt
class CheckEmail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        email = request.GET.get('email')
        user = UserAccount.objects.filter(email=email)
        if user:
            return Response(True)
        else:
            return Response(False)


class UserAccountViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer