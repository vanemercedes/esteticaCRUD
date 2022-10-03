from rest_framework import routers
from .viewsets import ProductosViewSet, VentasViewSet

router= routers.SimpleRouter()
router.register('productos',ProductosViewSet)
router.register('ventas',VentasViewSet)


urlpatterns = router.urls