from rest_framework import viewsets, status
from rest_framework.response import Response
from contents.models.metadata import MetaDataField
from contents.models.content_type import ContentType
from contents.serializers.metadata import MetaDataFieldSerializer
from rest_framework.generics import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(
        summary="List all metadata fields",
        description="Retrieve a list of all metadata fields.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a metadata field",
        description="Retrieve a specific metadata field by ID.",
    ),
    create=extend_schema(
        summary="Create a new metadata field",
        description="Create a new metadata field.",
    ),
    update=extend_schema(
        summary="Update a metadata field",
        description="Update an existing metadata field.",
    ),
    partial_update=extend_schema(
        summary="Partially update a metadata field",
        description="Partially update an existing metadata field.",
    ),
    destroy=extend_schema(
        summary="Delete a metadata field", description="Delete a metadata field."
    ),
)
class MetaDataFieldViewSet(viewsets.ModelViewSet):
    serializer_class = MetaDataFieldSerializer

    def get_queryset(self):
        content_type = get_object_or_404(ContentType, id=self.kwargs["content_type_pk"])
        return MetaDataField.objects.filter(content_type=content_type)

    def perform_create(self, serializer):
        content_type = get_object_or_404(ContentType, id=self.kwargs["content_type_pk"])
        serializer.save(content_type=content_type)

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            # If the input data is a list, handle bulk creation
            content_type = get_object_or_404(ContentType, id=kwargs["content_type_pk"])
            serializers = [self.get_serializer(data=data) for data in request.data]
            for serializer in serializers:
                serializer.is_valid(raise_exception=True)
                serializer.save(content_type=content_type)
            return Response(
                [serializer.data for serializer in serializers],
                status=status.HTTP_201_CREATED,
            )
        else:
            return super().create(request, *args, **kwargs)
