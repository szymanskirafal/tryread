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
        'books',
        view=views.WriterBooksListView.as_view(),
        name='books'
    ),
    path(
        '<slug:slug>/<int:pk>/',
        view=views.WriterBookDetailView.as_view(),
        name='book'
    ),

    path(
        '<slug:slug>/chapter-create/<int:pk>/',
        view=views.WriterChapterCreateView.as_view(),
        name='chapter_create'
    ),
    path(
        '<slug:slug>/<slug:slug_chapter>/<int:pk>/',
        view=views.WriterChapterDetailView.as_view(),
        name='chapter'
    ),
    path(
        '<slug:slug>/<slug:slug_chapter>/text-create/<int:pk>/',
        view=views.WriterTextCreateView.as_view(),
        name='text_create'
    ),
    path(
        '<slug:slug>/<slug:slug_chapter>/section/<int:pk>/',
        view=views.WriterSectionDetailView.as_view(),
        name='section_detail'
    ),
    path(
        '<slug:slug>/<slug:slug_chapter>/section/update/<int:pk>/',
        view=views.WriterSectionUpdateView.as_view(),
        name='section_update'
    ),
    path(
        '<slug:slug>/<slug:slug_chapter>/section/delete/<int:pk>/',
        view=views.WriterSectionDeleteView.as_view(),
        name='section_delete'
    ),


]
