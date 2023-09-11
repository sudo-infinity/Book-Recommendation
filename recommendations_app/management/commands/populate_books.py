from django.core.management.base import BaseCommand
from recommendations_app.models import Genre, Author, Book

class Command(BaseCommand):
    help = 'Populate the database with books, genres, and authors'

    def handle(self, *args, **kwargs):
        # Create genres
        genre1 = Genre.objects.create(name='Science Fiction')
        genre2 = Genre.objects.create(name='Mystery')
        
        # Create authors
        author1 = Author.objects.create(name='Isaac Asimov')
        author2 = Author.objects.create(name='Agatha Christie')
        
        # Create books and associate them with genres and authors
        book1 = Book.objects.create(
            title='Foundation',
            author=author1,
            synopsis='A science fiction novel...',
            cover_image_url='https://example.com/image1.jpg',
        )
        book1.genre.add(genre1)  # Add genres using many-to-many relationship

        book2 = Book.objects.create(
            title='Murder on the Orient Express',
            author=author2,
            synopsis='A mystery novel...',
            cover_image_url='https://example.com/image2.jpg',
        )
        book2.genre.add(genre2)

        self.stdout.write(self.style.SUCCESS('Database populated with books, genres, and authors'))
