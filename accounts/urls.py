from django.urls import include, path


from .views import CheckEmail, ListUserAccounts, DeleteUserAccount, UpdateUserAccount


urlpatterns = [
    path('users/check_email/', CheckEmail.as_view(), name="check_email"),
    path('users/', ListUserAccounts.as_view(), name="list-users"),
    path('users/delete/<int:id>/', DeleteUserAccount.as_view(), name="delete_user"),
    path('users/update/<int:id>/', UpdateUserAccount.as_view(), name="update_user"),
]
