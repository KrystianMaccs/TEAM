from TEAM.settings.base import AUTH_USER_MODEL
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedUUIDModel


class Posts(TimeStampedUUIDModel):
    author = models.ForeignKey(AUTH_USER_MODEL, related_name = _("post"),
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name=_("Title"), default="What's your theory?")
    body = models.TextField(verbose_name=_("Body"))
    likes = models.ManyToManyField(AUTH_USER_MODEL, related_name="likes")
    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    author = models.CharField(max_length = 50)
    body = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name= 'comments')
    
    def __str__(self):
        return self.body