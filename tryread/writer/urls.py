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
        '<slug:slug>/<slug:slug_chapter>/update/<int:pk>/',
        view=views.WriterChapterUpdateView.as_view(),
        name='chapter-update'
    ),
    path(
        '<slug:slug>/<slug:slug_chapter>/preview/<int:pk>/',
        view=views.WriterChapterPreviewDetailView.as_view(),
        name='chapter-preview'
    ),
    path(
        '<slug:slug>/<slug:slug_chapter>/text-create/<int:pk>/',
        view=views.WriterTextCreateView.as_view(),
        name='text_create'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/<int:pk_chapter>/update-text/<int:pk>/',
        view=views.WriterTextUpdateView.as_view(),
        name='text-update'
    ),

    path(
        '<slug:slug>/<slug:slug_chapter>/add-picture/<int:pk>/',
        view=views.WriterAddPictureCreateView.as_view(),
        name='add_picture'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/<int:pk_chapter>/delete-picture/<int:pk_picture>/',
        view=views.WriterPictureDeleteView.as_view(),
        name='picture-delete'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/<int:pk_chapter>/picture-update/<int:pk>/',
        view=views.WriterPictureUpdateView.as_view(),
        name='picture-update'
    ),


]
