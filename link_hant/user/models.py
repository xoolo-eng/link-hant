import os
import traceback
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver
from PIL import Image


# class DelQuerySet(models.query.QuerySet):
#     def delete(self):
#         print("DELETE")
#         print(self)
#         print(len(self))
#         for el in self:
#             el.delete()


# class DelManager(BaseUserManager):
#     def get_query_set(self):
#         return DelQuerySet(self.model, using=self._db)


class User(AbstractUser):
    def path_upload(self, filename):
        type_file = "." + filename.split(".")[-1]
        return os.path.join(
            "users",
            "avatars",
            self.username + type_file,
        )

    phone = models.CharField(
        null=True,
        max_length=20,
        verbose_name="User phone number.",
    )
    sex = models.CharField(
        null=True,
        max_length=1,
        verbose_name="Sex.",
    )
    avatar = models.ImageField(
        upload_to=path_upload,
        null=True,
        verbose_name="Avatar",
    )

    # objects = DelManager()

    def __str__(self):
        return self.username


@receiver(post_delete, sender=User)
def clean_avatars(sender, instance, **kwargs):
    instance.avatar.delete(False)


@receiver(post_save, sender=User)
def process_image(sender, instance, **kwargs):
    img_path = os.path.join(settings.MEDIA_ROOT, instance.avatar.path)
    image = Image.open(img_path).convert('LA')
    image.show()