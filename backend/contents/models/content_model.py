from django.db import models


class Content(models.Model):
    CONTENT_TYPES = [
        ("book", "Book"),
        ("paper", "Paper"),
        ("blog_post", "Blog Post"),
        ("md_file", "Markdown File"),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
