from rest_framework import viewsets
from ..models.content import Content
from ..serializers.content import ContentSerializer
from django.contrib.postgres.search import SearchVector
from rest_framework.generics import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(
        summary="List all contents", description="Retrieve a list of all contents."
    ),
    retrieve=extend_schema(
        summary="Retrieve a content", description="Retrieve a specific content by ID."
    ),
    create=extend_schema(
        summary="Create a new content", description="Create a new content."
    ),
    update=extend_schema(
        summary="Update a content", description="Update an existing content."
    ),
    partial_update=extend_schema(
        summary="Partially update a content",
        description="Partially update an existing content.",
    ),
    destroy=extend_schema(summary="Delete a content", description="Delete a content."),
)
class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        content = serializer.save()
        content.search_vector = SearchVector("title", weight="A") + SearchVector(
            "author", weight="B"
        )
        content.save()

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {"id": self.kwargs["pk"]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj
