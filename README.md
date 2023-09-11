# Book Recommendation System

The Book Recommendation System is a web application that allows users to discover and manage their favorite books. This project is built using Django, a high-level Python web framework, and provides features like user registration, book search, user profiles, and book interactions.

## Features

- User Registration: Users can create accounts and log in to access personalized features.
- Book Search: Users can search for books by title, genre, author, and rating.
- User Profiles: Users can customize their profiles, including favorite genres, authors, and books.
- Book Interactions: Users can mark books as "Read," "Want to Read," or "Currently Reading" and track their reading progress.
- User Comments and Ratings: Users can comment on and rate books to share their opinions and recommendations with others.
- Responsive Design: The application is responsive and works well on both desktop and mobile devices.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- Django 3.2+
- Virtualenv (optional but recommended)

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/book-recommendation-system.git
   cd book-recommendation-system

2. Create a virtual environment (optional but recommended):

   ```bash
  virtualenv venv source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Apply database migrations:
    ```bash
    python manage.py migrate

4. Create a superuser account (admin):
    ```bash
    python manage.py createsuperuser

5. Start the development server:
    ```bash
    python manage.py runserver

6. Access the admin interface at http://127.0.0.1:8000/admin/ to add books, genres, authors, and perform other administrative tasks.

### Applying Seed Data
To populate the database with sample books, genres, and authors, you can use the provided seed management command. Run the following command:
    python manage.py populate_books



This command will create sample data for your application.

## Usage

1. Visit http://127.0.0.1:8000/ in your web browser to access the Book Recommendation System.

2. Register or log in to your account to start using the features.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the project on GitHub.
Create a new branch for your feature or bug fix.
Make your changes and ensure that the code passes all tests.
Create a pull request with a detailed description of your changes.
