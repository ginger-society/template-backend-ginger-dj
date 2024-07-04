
from ginger.urls import path
from ginger.rest_framework.routers import DefaultRouter

# pylint:disable=E0401
from .views import *


router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')


urlpatterns = [
    path("health-check", health_check_view),
    path("test/", test_view),
    path("test2/", test_view2),
] + router.urls
