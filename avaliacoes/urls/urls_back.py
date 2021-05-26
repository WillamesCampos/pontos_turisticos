from django.urls import include
from django.urls.conf import path
from rest_framework import routers

from avaliacoes.viewsets import AvaliacaoViewSet

router = routers.SimpleRouter()

router.register(
    'avaliacoes',
    AvaliacaoViewSet,
    basename='avaliacoes'
)

urlpatterns = [
    path('backend/', include(router.urls))
]
