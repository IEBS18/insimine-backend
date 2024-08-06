from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogListCreateView, BlogDetailView, ContentBlockListCreateView, ContentBlockDetailView, ServiceListCreateView, ServiceDetailView, TechStackViewSet, ClientViewSet, FormDataCreateView, CaseStudyDetailView, CaseStudyListCreateView, WhitePaperListCreateView, WhitePaperDetailView

router = DefaultRouter()
router.register(r'techstack', TechStackViewSet)
router.register(r'client', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('case-studies/', CaseStudyListCreateView.as_view(), name='case-study-list-create'),
    path('case-studies/<int:pk>/', CaseStudyDetailView.as_view(), name='case-study-detail'),
    path('content-blocks/', ContentBlockListCreateView.as_view(), name='contentblock-list-create'),
    path('content-blocks/<int:pk>/', ContentBlockDetailView.as_view(), name='contentblock-detail'),
    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('form-submit/', FormDataCreateView.as_view(), name='form-submit'),
    path('whitepapers/', WhitePaperListCreateView.as_view(), name='whitepaper-list-create'),
    path('whitepapers/<int:pk>/', WhitePaperDetailView.as_view(), name='whitepaper-detail'),
]
