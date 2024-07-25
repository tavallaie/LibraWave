from django.db import models


class TextContent(models.Model):
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.content[:50]  # Display the first 50 characters
