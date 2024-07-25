from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import ContentTypeViewSet, ContentViewSet, MetaDataFieldViewSet

router = DefaultRouter()
router.register(r"content-types", ContentTypeViewSet, basename="content-type")
router.register(r"contents", ContentViewSet, basename="content")

content_type_router = NestedSimpleRouter(
    router, r"content-types", lookup="content_type"
)
content_type_router.register(
    r"metadata-fields", MetaDataFieldViewSet, basename="metadata-field"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(content_type_router.urls)),
]
