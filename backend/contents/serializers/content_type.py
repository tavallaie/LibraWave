from rest_framework import serializers
from contents.models.content_type import ContentType
from contents.models.metadata import MetaDataField


class MetaDataFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaDataField
        fields = ["id", "name", "field_type", "required"]


class ContentTypeSerializer(serializers.ModelSerializer):
    metadata_fields = MetaDataFieldSerializer(many=True, required=False)

    class Meta:
        model = ContentType
        fields = ["id", "name", "metadata_fields"]

    def create(self, validated_data):
        metadata_fields_data = validated_data.pop("metadata_fields", [])
        content_type = ContentType.objects.create(**validated_data)
        for field_data in metadata_fields_data:
            MetaDataField.objects.create(content_type=content_type, **field_data)
        return content_type
