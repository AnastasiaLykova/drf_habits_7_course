from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'is_active', 'telegram',)
    list_filter = ('email',)
    search_fields = ('email',)
