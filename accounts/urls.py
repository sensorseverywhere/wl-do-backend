from django.urls import include, path
from rest_framework import routers

from .views import CheckEmail, UserAccountViewSet

router = routers.DefaultRouter()
router.register(r'users', UserAccountViewSet)

urlpatterns = [
    path('users/check_email/', CheckEmail.as_view(), name="check_email"),
    path('', include(router.urls)),
]
