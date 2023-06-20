from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from posts.models import Posts


class Comment(models.Model):
    comment_name = models.CharField(max_length=150, verbose_name="Name")
    comment_email = models.EmailField(verbose_name="E-mail")
    comment = models.TextField(verbose_name="Comment")
    comment_post = models.ForeignKey(
        Posts, on_delete=models.CASCADE, verbose_name="Post"
    )
    comment_user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="User"
    )
    comment_date = models.DateTimeField(default=timezone.now, verbose_name="Date")
    comment_published = models.BooleanField(default=False, verbose_name="Published")

    def __str__(self) -> str:
        return self.comment_name
