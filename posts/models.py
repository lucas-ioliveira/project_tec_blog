from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms

# Ciação das classes categorias e post


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    # Representando a classe (objeto)
    def __str__(self):
        return self.nome


class Posts(models.Model):
    post_title = models.CharField(max_length=255, verbose_name="Title")
    post_author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="Author"
    )
    post_date = models.DateTimeField(default=timezone.now, verbose_name="Date")
    post_content = models.TextField(verbose_name="Content")
    post_excerpt = models.TextField(verbose_name="Excerpt")
    post_category = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        verbose_name="Category",
    )
    post_image = models.ImageField(
        upload_to="post_img/%Y/%m/", blank=True, null=True, verbose_name="Image"
    )
    post_published = models.BooleanField(default=False, verbose_name="Published")

    def __str__(self) -> str:
        return self.post_title
