from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from .content_type import ContentType
from .text_content import TextContent
from .file_content import FileContent


class Content(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content_type = models.ForeignKey(
        ContentType, related_name="contents", on_delete=models.CASCADE
    )
    publication_date = models.DateField(null=True, blank=True)
    license = models.CharField(max_length=255, null=True, blank=True)
    search_vector = SearchVectorField(null=True, blank=True)
    text_contents = models.ManyToManyField(
        TextContent, through="ContentTextRelation", related_name="contents"
    )
    file_contents = models.ManyToManyField(
        FileContent, through="ContentFileRelation", related_name="contents"
    )

    def __str__(self):
        return self.title

    class Meta:
        indexes = [GinIndex(fields=["search_vector"])]


class ContentTextRelation(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    text_content = models.ForeignKey(TextContent, on_delete=models.CASCADE)


class ContentFileRelation(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    file_content = models.ForeignKey(FileContent, on_delete=models.CASCADE)
