from rest_framework import serializers
from contents.models.content import Content
from contents.models.metadata import MetaDataValue, MetaDataField
from contents.models.text_content import TextContent
from contents.models.file_content import FileContent
from contents.models.content_type import ContentType
from django.contrib.postgres.search import SearchVector


class MetaDataValueSerializer(serializers.ModelSerializer):
    field_name = serializers.SlugRelatedField(
        slug_field="name", queryset=MetaDataField.objects.all(), source="field"
    )
    field_type = serializers.ReadOnlyField(source="field.field_type")

    class Meta:
        model = MetaDataValue
        fields = ["field_name", "field_type", "value"]


class TextContentSerializer(serializers.ModelSerializer):
    metadata_values = MetaDataValueSerializer(many=True, required=False)

    class Meta:
        model = TextContent
        fields = ["id", "content", "metadata_values"]


class FileContentSerializer(serializers.ModelSerializer):
    metadata_values = MetaDataValueSerializer(many=True, required=False)

    class Meta:
        model = FileContent
        fields = ["id", "file", "metadata_values"]


class ContentSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        slug_field="name", queryset=ContentType.objects.all()
    )
    metadata_values = MetaDataValueSerializer(many=True, required=False)
    text_contents = TextContentSerializer(many=True, required=False)
    file_contents = FileContentSerializer(many=True, required=False)

    class Meta:
        model = Content
        fields = [
            "id",
            "title",
            "author",
            "content_type",
            "text_contents",
            "file_contents",
            "publication_date",
            "license",
            "metadata_values",
        ]

    def validate(self, data):
        # Get content type and associated metadata fields
        content_type = data.get("content_type")
        metadata_values_data = data.get("metadata_values", [])

        # Check for required metadata fields
        required_fields = MetaDataField.objects.filter(
            content_type=content_type, required=True
        )
        provided_field_names = [mv["field"].name for mv in metadata_values_data]

        for required_field in required_fields:
            if required_field.name not in provided_field_names:
                raise serializers.ValidationError(
                    f"Missing required metadata field: {required_field.name}"
                )

        return data

    def create(self, validated_data):
        text_contents_data = validated_data.pop("text_contents", [])
        file_contents_data = validated_data.pop("file_contents", [])
        metadata_values_data = validated_data.pop("metadata_values", [])

        content = Content.objects.create(**validated_data)

        for text_data in text_contents_data:
            text_content_data = text_data
            text_content = TextContent.objects.create(**text_content_data)
            content.text_contents.add(text_content)

        for file_data in file_contents_data:
            file_content_data = file_data
            file_content = FileContent.objects.create(**file_content_data)
            content.file_contents.add(file_content)

        for value_data in metadata_values_data:
            field = value_data.pop("field")
            MetaDataValue.objects.create(content=content, field=field, **value_data)

        # Update the search vector
        content.search_vector = SearchVector("title", weight="A") + SearchVector(
            "author", weight="B"
        )
        content.save()

        return content

    def update(self, instance, validated_data):
        text_contents_data = validated_data.pop("text_contents", [])
        file_contents_data = validated_data.pop("file_contents", [])
        metadata_values_data = validated_data.pop("metadata_values", [])

        instance = super().update(instance, validated_data)

        for text_data in text_contents_data:
            text_content_data = text_data
            if "id" in text_content_data:
                text_content = TextContent.objects.get(id=text_content_data["id"])
                text_content.content = text_content_data["content"]
                text_content.save()
            else:
                text_content = TextContent.objects.create(**text_content_data)
                instance.text_contents.add(text_content)

        for file_data in file_contents_data:
            file_content_data = file_data
            if "id" in file_content_data:
                file_content = FileContent.objects.get(id=file_content_data["id"])
                file_content.file = file_content_data["file"]
                file_content.save()
            else:
                file_content = FileContent.objects.create(**file_content_data)
                instance.file_contents.add(file_content)

        for value_data in metadata_values_data:
            field = value_data.pop("field")
            MetaDataValue.objects.update_or_create(
                content=instance, field=field, defaults={"value": value_data["value"]}
            )

        # Update the search vector
        instance.search_vector = SearchVector("title", weight="A") + SearchVector(
            "author", weight="B"
        )
        instance.save()

        return instance
