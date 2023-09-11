from django.contrib import admin
from .models import Book # import only those Models you need in a particular class
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre_list', 'cover_image_url')
    list_filter = ('genre',)
    search_fields = ('title', 'author__name', 'genre__name')

    def genre_list(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])
    genre_list.short_description = 'Genres'