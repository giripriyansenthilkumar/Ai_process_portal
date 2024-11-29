from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_number', 'document_file', 'uploaded_at')
    search_fields = ('document_number',)
