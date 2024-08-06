from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from .models import Blog, Service, TechStack, Client, ContentBlock, FormData, CaseStudy, WhitePaper
from .serializers import BlogSerializer, ServiceSerializer, TechStackSerializer, ClientSerializer, ContentBlockSerializer, FormDataSerializer, CaseStudySerializer, WhitePaperSerializer

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CaseStudyListCreateView(generics.ListCreateAPIView):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer

class CaseStudyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer

class ContentBlockListCreateView(generics.ListCreateAPIView):
    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockSerializer

class ContentBlockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockSerializer

class FormDataCreateView(generics.CreateAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class TechStackViewSet(viewsets.ModelViewSet):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer

class WhitePaperListCreateView(generics.ListCreateAPIView):
    queryset = WhitePaper.objects.all()
    serializer_class = WhitePaperSerializer

class WhitePaperDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WhitePaper.objects.all()
    serializer_class = WhitePaperSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer