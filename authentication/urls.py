from django.urls import path, include
from authentication.views import RegViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'signup', RegViewSet)

urlpatterns = [
    path('', include(router.urls))
]
