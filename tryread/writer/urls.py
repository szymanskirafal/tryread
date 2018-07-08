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
        name='book-create'
    ),
    path(
        'books',
        view=views.WriterBooksListView.as_view(),
        name='books'
    ),
    path(
        '<slug:slug_book>/<int:pk_book>/',
        view=views.WriterBookDetailView.as_view(),
        name='book'
    ),
    path(
        '<slug:slug_book>/<int:pk_book>/chapter-create/',
        view=views.WriterChapterCreateView.as_view(),
        name='chapter-create'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/<int:pk_chapter>/',
        view=views.WriterChapterDetailView.as_view(),
        name='chapter'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/update/<int:pk_chapter>/',
        view=views.WriterChapterUpdateView.as_view(),
        name='chapter-update'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/preview/<int:pk_chapter>/',
        view=views.WriterChapterPreviewUpdateView.as_view(),
        name='chapter-preview'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/<int:pk_chapter>/text-create/',
        view=views.WriterTextCreateView.as_view(),
        name='text-create'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/<int:pk_chapter>/text-delete/<int:pk_text>/',
        view=views.WriterTextDeleteView.as_view(),
        name='text-delete'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/<int:pk_chapter>/update-text/<int:pk_text>/',
        view=views.WriterTextUpdateView.as_view(),
        name='text-update'
    ),

    path(
        '<slug:slug_book>/<slug:slug_chapter>/<int:pk_chapter>/add-picture/',
        view=views.WriterPictureCreateView.as_view(),
        name='picture-create'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/<int:pk_chapter>/delete-picture/<int:pk_picture>/',
        view=views.WriterPictureDeleteView.as_view(),
        name='picture-delete'
    ),
    path(
        '<slug:slug_book>/<slug:slug_chapter>/<int:pk_chapter>/picture-update/<int:pk_picture>/',
        view=views.WriterPictureUpdateView.as_view(),
        name='picture-update'
    ),

]
