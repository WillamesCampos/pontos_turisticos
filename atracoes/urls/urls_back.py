from django.urls import include
from django.urls.conf import path
from rest_framework import routers
from atracoes.viewsets import AtracaoViewSet

router = routers.SimpleRouter()

router.register(
    'atracoes', AtracaoViewSet,
    basename='atracoes'
)

urlpatterns = [
    path('backend/', include(router.urls)),
]
