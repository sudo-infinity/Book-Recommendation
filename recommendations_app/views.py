from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UserProfileForm
from django.contrib import messages
from django.db.models import Q 
from .models import *


class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # Redirect to the login page upon successful registration

class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

@login_required
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            # Redirect to the profile page after saving changes
            return redirect('home')

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form})

@login_required
def recommend_books(request):
    user = request.user

    # Check if the user has preferences
    try:
        user_profile = UserProfile.objects.get(user=user)
        #import pdb;
        #pdb
        no_preferences = not (user_profile.favorite_genres.exists() or user_profile.favorite_authors.exists() or user_profile.favorite_books.exists())
    except UserProfile.DoesNotExist:
        no_preferences = True
        return render(request, 'recommendations.html', {'no_preferences': no_preferences})
    
    genre_recommendations = Book.objects.filter(genre__in=user_profile.favorite_genres.all())

    # Recommendation based on favorite authors
    author_recommendations = Book.objects.filter(author__in=user_profile.favorite_authors.all())

    # Recommendation based on similar users' preferences (you may need to refine this part)
    similar_users = UserProfile.objects.filter(
        favorite_genres__in=user_profile.favorite_genres.all(),
        favorite_authors__in=user_profile.favorite_authors.all(),
    ).exclude(user=request.user)

    similar_user_recommendations = Book.objects.filter(userprofile__in=similar_users)

    # Combine and deduplicate recommendations
    recommended_books = (genre_recommendations | author_recommendations | similar_user_recommendations).distinct()

    # Render the user profile page with recommendations
    return render(request, 'recommendations.html', {'recommended_books': recommended_books, 'no_preferences': no_preferences})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user_interaction = None  # Retrieve user interaction for this book, if applicable

    if request.user.is_authenticated:
        user_interaction = UserInteraction.objects.filter(user=request.user, book=book).first()

    context = {
        'book': book,
        'user_interaction': user_interaction,  # Include user_interaction in the context
    }

    return render(request, 'book_detail.html', context)

@login_required
def book_search(request):
    # Get search query and filter criteria from the request
    search_query = request.GET.get('q')
    selected_genre = request.GET.get('genre')
    selected_author = request.GET.get('author')
    selected_rating = request.GET.get('rating')

    # Build the initial queryset
    books = Book.objects.all()

    # Apply filters based on criteria
    if search_query:
        # Apply case-insensitive search filter
        books = books.filter(Q(title__icontains=search_query) | Q(title__iexact=search_query))

    if selected_genre:
        # Apply case-insensitive genre filter
        books = books.filter(genre__name__iexact=selected_genre)

    if selected_author:
        # Apply case-insensitive author filter
        books = books.filter(author__name__iexact=selected_author)

    if selected_rating:
        # Apply rating filter
        books = books.filter(rating__gte=selected_rating)

    return render(request, 'book_search.html', {'books': books})

@login_required
def manage_interaction(request, book_id, interaction_type):
    user = request.user
    book = get_object_or_404(Book, id=book_id)

    # Check if the user has already interacted with this book
    user_interaction, created = UserInteraction.objects.get_or_create(
        user=user,
        book=book
    )

    # Update the status based on the interaction_type
    user_interaction.status = interaction_type

    # Validate and update progress (example: limit progress to 0-100)
    progress = request.POST.get('progress')
    if progress is not None:
        try:
            progress = int(progress)
            if 0 <= progress <= 100:
                user_interaction.progress = progress
        except ValueError:
            pass  # Handle invalid progress value gracefully

    user_interaction.save()

    messages.success(request, f'Your interaction with {book.title} has been updated.')

    return redirect('book_detail', book_id=book_id)

