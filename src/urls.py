
from ginger.urls import path

# pylint:disable=E0401
from .views import *


urlpatterns = [
    path("health-check", health_check_view),
    path("test/", test_view),
    path("test2/", test_view2),
]
