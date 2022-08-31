from django.urls import path

from .views import CheckEmail

urlpatterns = [
    path('users/check_email/', CheckEmail.as_view(), name="check_email"),
]
