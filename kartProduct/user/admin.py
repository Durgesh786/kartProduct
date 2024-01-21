from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # Fields to display in the list view


admin.site.register(User, UserAdmin)
