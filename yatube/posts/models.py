from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:10]


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
    )
    slug = models.SlugField(
        max_length=200,
        unique=True
    )
    description = models.TextField()

    def __str__(self):
        return self.title