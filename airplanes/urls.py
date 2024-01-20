from rest_framework.routers import DefaultRouter

from airplanes.views import AirplaneViewset

router = DefaultRouter()
router.register("airplanes", AirplaneViewset)

urlpatterns = router.urls
