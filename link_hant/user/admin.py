from django.contrib import admin
from user.models import User


class AdminUser(admin.ModelAdmin):

    list_display = ("username", "last_login")
    readonly_fields = ("username",)
    list_filter = (
        "username",
        "is_staff",
        "last_login",
    )
    search_fields = ('username', 'first_name',)
    fieldsets = (
        (
            None,
            {
                "fields": (
                   "username",
                   "sex",
                   "last_login"
                )
            },
        ),
    )








admin.site.register(User, AdminUser)