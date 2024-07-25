from django.contrib import admin
from .models import (
    ContentType,
    Content,
    TextContent,
    FileContent,
    MetaDataField,
    MetaDataValue,
    ContentTextRelation,
    ContentFileRelation,
)
from django import forms


class MetaDataValueInlineForm(forms.ModelForm):
    class Meta:
        model = MetaDataValue
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["value"].required = False


class MetaDataValueInline(admin.TabularInline):
    model = MetaDataValue
    form = MetaDataValueInlineForm
    extra = 1


class ContentTextRelationInline(admin.TabularInline):
    model = ContentTextRelation
    extra = 1


class ContentFileRelationInline(admin.TabularInline):
    model = ContentFileRelation
    extra = 1


class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ContentAdminForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "text_contents" in self.fields:
            self.fields["text_contents"].required = False
        if "file_contents" in self.fields:
            self.fields["file_contents"].required = False


class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm
    list_display = ("title", "author", "content_type", "publication_date", "license")
    search_fields = ("title", "author")
    list_filter = ("content_type", "publication_date")
    inlines = [
        ContentTextRelationInline,
        ContentFileRelationInline,
        MetaDataValueInline,
    ]


class TextContentAdmin(admin.ModelAdmin):
    list_display = ("content",)
    search_fields = ("content",)
    inlines = [MetaDataValueInline]


class FileContentAdmin(admin.ModelAdmin):
    list_display = ("file",)
    search_fields = ("file",)
    inlines = [MetaDataValueInline]


class MetaDataFieldAdmin(admin.ModelAdmin):
    list_display = ("name", "field_type", "content_type", "required")
    search_fields = ("name",)
    list_filter = ("content_type", "field_type", "required")


admin.site.register(ContentType, ContentTypeAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(TextContent, TextContentAdmin)
admin.site.register(FileContent, FileContentAdmin)
admin.site.register(MetaDataField, MetaDataFieldAdmin)
