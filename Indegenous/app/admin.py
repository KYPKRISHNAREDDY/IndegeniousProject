from django.contrib import admin

from .models import Element

@admin.register(Element)
class ModelElement(admin.ModelAdmin):
    list_display=['id','Name','Text']