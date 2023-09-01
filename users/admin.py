from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import City, CustomUser


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name')
    search_fields = ('id', 'city_name')
    list_filter = ('id', 'city_name')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    search_fields = ('id', 'email', 'first_name', 'last_name')
    list_filter = ('id', 'email', 'first_name', 'last_name')
    exclude = [
        'date_joined',
        'last_login',
        'groups',
        'user_permissions'
    ]


admin.site.unregister(Group)
