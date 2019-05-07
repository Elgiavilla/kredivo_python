from django.conf.urls import url
from rest_framework import routers
from kredivo.contact.views import ContactViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)

schema_docs_view = get_swagger_view(title = "Kredivo Test")

urlpatterns = [
    url(r'^docs/', schema_docs_view)
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)