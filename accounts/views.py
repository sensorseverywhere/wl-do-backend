from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

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


class ListUserAccounts(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        users = UserAccount.objects.all()
        serializer = UserAccountSerializer(users, many=True)
        return Response(serializer.data)


class DeleteUserAccount(APIView):
    permission_classes = [IsAdminUser]
    def delete(self, request, id):
        user = UserAccount.objects.get(id=id)
        user.delete()
        serializer = UserAccountSerializer
        return Response('User deleted')


class UpdateUserAccount(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, id):
        return UserAccount.objects.get(pk=id)

    def patch(self, request, id):
        user = self.get_object(id)
        serializer = UserAccountSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
           serializer.save()

           return Response(serializer.data) 
        return Response('User updated')