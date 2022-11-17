from django.contrib import admin

from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_staff')

admin.site.register(UserAccount, UserAccountAdmin)
