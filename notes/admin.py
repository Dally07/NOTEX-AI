from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'phrase','category', 'creat_at')
    search_fields = ('phrase', 'category')
    list_filter = ('category', 'creat_at')
    ordering = ('creat_at')
    ordering = ['id'] 
