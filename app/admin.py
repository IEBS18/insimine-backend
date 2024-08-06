from django.contrib import admin
from .models import Blog, Service, TechStack, Client, ContentBlock, CaseStudy, WhitePaper
# Register your models here.

class ContentBlockInline(admin.StackedInline):
    model = ContentBlock
    extra = 1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [ContentBlockInline]
    list_display = ('title', 'created_at', 'updated_at')

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    inlines = [ContentBlockInline]
    list_display = ('title', 'created_at', 'updated_at')
# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title','created_at','updated_at')
#     search_fields = ('title',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','desc')
    search_fields = ('name',)

@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ('name',)

@admin.register(WhitePaper)
class WhitePaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
