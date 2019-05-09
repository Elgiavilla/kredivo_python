from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from kredivo.contact import factories
from django.urls import path

schema_docs_view = get_swagger_view(title = "Kredivo Test")

urlpatterns = [
    path(r'contact/docs/', schema_docs_view),
    # path(r'contact/', views.ContactView.as_view()),
    # path('contact/<int:pk>/', views.ContactDetail.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)