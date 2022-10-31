from email.policy import default
from tabnanny import verbose
from TEAM.settings.base import AUTH_USER_MODEL
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile


class Posts(TimeStampedUUIDModel):
    author = models.ForeignKey(AUTH_USER_MODEL, related_name = _("post"),
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name=_("Title"), default="What's your theory?")
    post = models.TextField(verbose_name=_("Post"))