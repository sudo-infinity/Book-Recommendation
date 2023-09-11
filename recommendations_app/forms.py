from django import forms
from .models import UserProfile, Book

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['favorite_genres', 'favorite_authors', 'favorite_books']

        favorite_books = forms.ModelMultipleChoiceField(
            queryset=Book.objects.all(),  # Provide a queryset of all available books
            widget=forms.CheckboxSelectMultiple,  # Use checkboxes for book selection
            required=False,  # Make the field optional
        )
