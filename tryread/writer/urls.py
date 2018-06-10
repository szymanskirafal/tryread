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
        'add-book',
        view=views.WriterAddBookCreateView.as_view(),
        name='add_book'
    ),
    path(
        '<slug:slug>/',
        view=views.WriterBookDetailView.as_view(),
        name='book'
    ),
    path(
        '<slug:slug>/add-chapter/',
        view=views.WriterAddChapterCreateView.as_view(),
        name='add_chapter'
    ),
    path(
        '<slug:slug>/<slug:slug_chapter>/',
        view=views.WriterChapterDetailView.as_view(),
        name='chapter'
    ),
    path(
        '<slug:slug>/<slug:slug_chapter>/add-text/',
        view=views.WriterAddTextCreateView.as_view(),
        name='add_text'
    ),
    path(
        'books',
        view=views.WriterBooksListView.as_view(),
        name='books'
    ),

]
