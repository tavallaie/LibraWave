from django.db import models
from contents.models import Content
from django.contrib.auth.models import User


class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)  # e.g., page number or percentage

    def __str__(self):
        return f"{self.user.username} - {self.content.title} - {self.progress}"
