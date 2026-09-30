from django.contrib import admin # type: ignore
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'image', 'post', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('user__username',)
