from rest_framework import serializers
from contents.models.metadata import MetaDataField, MetaDataValue


class MetaDataFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaDataField
        fields = ["id", "name", "field_type", "required"]


class MetaDataValueSerializer(serializers.ModelSerializer):
    field_name = serializers.SlugRelatedField(
        slug_field="name", queryset=MetaDataField.objects.all(), source="field"
    )
    field_type = serializers.ReadOnlyField(source="field.field_type")

    class Meta:
        model = MetaDataValue
        fields = ["field_name", "field_type", "value"]
