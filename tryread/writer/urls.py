from django.urls import path

from . import views

app_name = "writer"
urlpatterns = [
    path(
        "",
        view=views.WriterTemplateView.as_view(),
        name="writer"
    ),
    path(
        "add-book",
        view=views.WriterAddBookCreateView.as_view(),
        name="add_book"
    ),
    path(
        "books",
        view=views.WriterBooksListView.as_view(),
        name="books"
    ),

]
