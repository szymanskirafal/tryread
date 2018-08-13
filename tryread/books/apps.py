from django.apps import AppConfig


class BooksConfig(AppConfig):
    name = 'books'


class UsersConfig(AppConfig):
    name = "tryread.books"
    verbose_name = "Books"
