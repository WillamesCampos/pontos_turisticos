from django.urls import include
from django.urls.conf import path
from rest_framework import routers
from atracoes.viewsets import AtracoesViewSet

router = routers.SimpleRouter()

router.register(
    'atracoes', AtracoesViewSet,
    basename='atracoes-list'
)

urlpatterns = [
    path('backend/', include(router.urls)),
]
