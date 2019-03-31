from django.contrib import admin

from bulletin import models


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'content',
        'author',
        'updated_at'
    ]

# Register your models here.
