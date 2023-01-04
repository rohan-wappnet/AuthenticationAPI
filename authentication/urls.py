from django.urls import path, include
from authentication.views import RegViewSet, LoginTokenViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'signup', RegViewSet)
router.register(r'login ', LoginTokenViewSet, basename="login")

urlpatterns = [
    path('', include(router.urls)),

]
