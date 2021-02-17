from django.db import models
from django.contrib.auth.models import AbstractUser


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
        verbose_name="Avatar",
    )

    def __str__(self):
        return self.username
