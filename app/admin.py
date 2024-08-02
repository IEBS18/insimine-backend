from django.contrib import admin
from .models import Blog, Service, TechStack, Client, Hero
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at')
    search_fields = ('title',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','desc')
    search_fields = ('name',)

@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading', 'image')
    search_fields = ('heading', 'subheading')