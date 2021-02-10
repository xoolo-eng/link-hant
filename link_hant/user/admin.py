from django.contrib import admin
from user.models import User


class AdminUser(admin.ModelAdmin):

    class Meta:
        fields = ["username", "last_login"]


admin.site.register(User, AdminUser)