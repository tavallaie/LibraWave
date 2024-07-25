from rest_framework import viewsets
from contents.models.content_type import ContentType
from contents.serializers.content_type import ContentTypeSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(
        summary="List all content types",
        description="Retrieve a list of all content types.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a content type",
        description="Retrieve a specific content type by ID.",
    ),
    create=extend_schema(
        summary="Create a new content type", description="Create a new content type."
    ),
    update=extend_schema(
        summary="Update a content type", description="Update an existing content type."
    ),
    partial_update=extend_schema(
        summary="Partially update a content type",
        description="Partially update an existing content type.",
    ),
    destroy=extend_schema(
        summary="Delete a content type", description="Delete a content type."
    ),
)
class ContentTypeViewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
