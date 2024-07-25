from django.db import models


class FileContent(models.Model):
    file = models.FileField(upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return self.file.name
