from django.contrib import admin
from .models import Video

# Register your models here.

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader', 'uploaded_at')
    search_fields = ('title', 'uploader__username')