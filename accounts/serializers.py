from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

from .models import UserAccount

User = get_user_model()


class UserCreateSerialzer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'is_staff', 'password')


class UserAccountSerializer(serializers.ModelSerializer):
<<<<<<< HEAD

=======
>>>>>>> 005af2dc2f6e356d0dfcc5395dfd316e6836a514
    class Meta:
        model = UserAccount
        # fields = ('id', 'name', 'email', 'is_staff')
        exclude=('password',)