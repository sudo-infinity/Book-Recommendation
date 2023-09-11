from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('home/', home, name='home'),
    path('logout/', user_logout, name='logout'),
    path('', RedirectView.as_view(url='home/', permanent=False), name='root'),
    path('profile/', profile, name='profile'),
    path('recommendations/', recommend_books, name='recommendations'),
    path('book-detail/<int:book_id>/', book_detail, name='book_detail'),
    path('book-search/', book_search, name='book_search'),
    path('manage-interaction/<int:book_id>/<str:interaction_type>/', manage_interaction, name='manage_interaction'),
    # Add other app URLs as needed
]
