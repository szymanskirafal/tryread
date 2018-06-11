from django.urls import path

from . import views

app_name = "writer"
urlpatterns = [
    path(
        '',
        view=views.WriterTemplateView.as_view(),
        name='writer'
    ),
    path(
        'book-create/',
        view=views.WriterBookCreateView.as_view(),
        name='book_create'
    ),
    path(
        '<slug:slug>/<int:pk>/',
        view=views.WriterBookDetailView.as_view(),
        name='book'
    ),
    path(
        '<slug:slug>/<int:pk>/chapter-create/',
        view=views.WriterChapterCreateView.as_view(),
        name='chapter_create'
    ),
    path(
        '<slug:slug>/<slug:slug_chapter>/<int:pk>/',
        view=views.WriterChapterDetailView.as_view(),
        name='chapter'
    ),
    path(
        'chapter/<int:pk>/text-create/',
        view=views.WriterTextCreateView.as_view(),
        name='text_create'
    ),
    path(
        'books',
        view=views.WriterBooksListView.as_view(),
        name='books'
    ),

]
