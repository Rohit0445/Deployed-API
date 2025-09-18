from .views import StudentViewSet

# from rest_framework import routers
# router = routers.SimpleRouter()
# router.register(r'users', StudentViewSet)
# urlpatterns = router.urls

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', StudentViewSet, basename='student')
urlpatterns = router.urls