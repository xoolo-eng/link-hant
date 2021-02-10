from django.contrib import admin
from home.models import QuickContact


class AdminQuickContact(admin.ModelAdmin):
    list_display = ["email", "is_moderate"]


admin.site.register(QuickContact, AdminQuickContact)