from rest_framework import serializers
from .models import Blog, Service, TechStack, Client, ContentBlock, FormData, CaseStudy, WhitePaper

class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ['id', 'block_type', 'text', 'image', 'order']

class BlogSerializer(serializers.ModelSerializer):
    content_blocks = ContentBlockSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'created_at', 'updated_at', 'content_blocks']

class CaseStudySerializer(serializers.ModelSerializer):
    content_blocks = ContentBlockSerializer(many=True, read_only=True)

    class Meta:
        model = CaseStudy
        fields = ['id', 'title', 'created_at', 'updated_at', 'content_blocks']

class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        # fields = ['id', 'name', 'email', 'phone', 'additional_info', 'submitted_at']
        fields = ['id', 'name', 'email', 'phone', 'country', 'submitted_at']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'desc', 'image']

class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = '__all__'


class WhitePaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhitePaper
        fields = ['id', 'title', 'image', 'description', 'pdf']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

