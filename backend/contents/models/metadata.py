from django.db import models
from .content import Content
from .text_content import TextContent
from .file_content import FileContent
from .content_type import ContentType


class MetaDataField(models.Model):
    FIELD_TYPES = [
        ("char", "CharField"),
        ("text", "TextField"),
        ("int", "IntegerField"),
        ("float", "FloatField"),
        ("date", "DateField"),
        ("datetime", "DateTimeField"),
        ("bool", "BooleanField"),
        ("email", "EmailField"),
        ("url", "URLField"),
    ]

    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50, choices=FIELD_TYPES)
    content_type = models.ForeignKey(
        ContentType, related_name="metadata_fields", on_delete=models.CASCADE
    )
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MetaDataValue(models.Model):
    content = models.ForeignKey(
        Content,
        related_name="metadata_values",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    text_content = models.ForeignKey(
        TextContent,
        related_name="metadata_values",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    file_content = models.ForeignKey(
        FileContent,
        related_name="metadata_values",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    field = models.ForeignKey(MetaDataField, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.field.name}: {self.value}"
