from django.db import models
from user.models import User


class Blog(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Record title.",
    )
    create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Create date.",
    )
    text = models.TextField(
        verbose_name="Record content.",
    )
    user = models.ForeignKey(
        User,
        related_name="blogs",
        verbose_name="User.",
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        "Tags",
        verbose_name="#hashtag",
        related_name="hashtags",
    )

    class Meta:
        db_table = "blogs"
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ("-create", "-id")

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(
        max_length=15,
        verbose_name="#hashtag",
    )

    class Meta:
        db_table = "tags"
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ("name",)

    def __str__(self):
        return self.name
    


class Comment(models.Model):
    email = models.EmailField(
        verbose_name="Commentator email.",
    )
    comment = models.TextField(
        verbose_name="Content.",
    )
    user = models.ForeignKey(
        User,
        related_name="comments",
        verbose_name="User.",
        on_delete=models.CASCADE,
    )
    create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created.",
    )
    is_moderated = models.BooleanField(
        default=False,
        verbose_name="Is modetated.",
    )

    def __str__(self):
        return self.user
