from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, ServiceViewSet, TechStackViewSet, ClientViewSet, HeroViewSet

router = DefaultRouter()
router.register(r'blog', BlogViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'techstack', TechStackViewSet)
router.register(r'client', ClientViewSet)
router.register(r'hero', HeroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
