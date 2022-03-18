from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор поста',
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        'Group',
        related_name='posts',
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
        verbose_name='Название группы',
        max_length=200,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Ссылка группы',
        max_length=200,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание группы',
    )

    def __str__(self):
        return self.title