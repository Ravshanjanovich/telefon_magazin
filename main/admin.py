from django.contrib import admin
from .models import Contact, Testemonial, History, About , Index 

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title','name','description',)
    list_display_links = ('title','name','description',)

@admin.register(Testemonial)
class TestemonialAdmin(admin.ModelAdmin):
    list_display = ('name','description','image',)
    list_display_links = ('name','description','image',)

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('title','description',)
    list_display_links = ('title','description',)

@admin.register(About)
class AboutAdmin(amdin.ModelAdmin):
    list_display = ('title','sub_title','image',)
    list_display_links = ('title','sub_title','image',)

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ('title','sub_title','image',)
    list_display_links = ('title','sub_title','image',)