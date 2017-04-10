from rest_framework.routers import SimpleRouter

from comentary.api import ComentaryViewSet

router = SimpleRouter()
router.register(r'^api/0.1/comentaries', ComentaryViewSet, 'Comentary')

urlpatterns = router.urls