from django.db import models


class QuickContact(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="User name.",
    )
    email = models.EmailField(
        verbose_name="User email.",
    )
    message = models.TextField(
        verbose_name="Message",
    )

    class Meta:
        db_table = "quick_contacts"
        verbose_name = "Quick Contact"
        verbose_name_plural = "Quick Contacts"

    def __str__(self):
        return self.name
        
