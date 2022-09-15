from django.urls import include, path


from .views import CheckEmail, ListUserAccounts, DeleteUserAccount


urlpatterns = [
    path('users/check_email/', CheckEmail.as_view(), name="check_email"),
    path('users/', ListUserAccounts.as_view(), name="list-users"),
    path('users/delete/<int:id>/', DeleteUserAccount.as_view(), name="delete_user"),
]
