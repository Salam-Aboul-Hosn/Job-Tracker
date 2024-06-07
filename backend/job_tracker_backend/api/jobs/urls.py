
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()
router.register(r'job', JobViewSet, basename='job')

urlpatterns = router.urls
