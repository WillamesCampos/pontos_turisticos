from django.urls.conf import path
from django.urls import include
from rest_framework import routers
from comentarios.viewsets import ComentarioViewSet

router = routers.SimpleRouter()

router.register(
    'comentarios',
    ComentarioViewSet,
    basename='comentarios'
)

urlpatterns = [
    path('backend/', include(router.urls)),
]
