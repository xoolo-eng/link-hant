from django.contrib import admin
from home.models import QuickContact


class AdminQuickContact(admin.ModelAdmin):
    list_display = ["name", "email"]


admin.site.register(QuickContact, AdminQuickContact)