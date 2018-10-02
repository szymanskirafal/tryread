from django.urls import path

from . import views

app_name = "read"
urlpatterns = [
    path("", view=views.ReadBooksListView.as_view(), name="books"),
    path(
        '<slug:slug_book>/<int:pk_book>/',
        view=views.ReadBookDetailView.as_view(),
        name='book-detail'
    ),
    path(
        '<slug:slug_book>/<int:pk_book>/<int:pk_chapter>/',
        view=views.ReadChapterDetailView.as_view(),
        name='chapter-detail'
    ),

]
