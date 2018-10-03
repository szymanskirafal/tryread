from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.views.generic.edit import FormMixin

from books.forms import BookFiltersForm
from books.models import Book, Chapter
from tryread.users.models import User
from writer.views import PicturesAndTextAsElementsMixin


class ReadBooksListView(LoginRequiredMixin, FormMixin, ListView):
    context_object_name = 'books'
    form_class = BookFiltersForm
    model = Book
    template_name = "read/books.html"

    def get_queryset(self):
        queryset = Book.objects.only('pk', 'author', 'title', 'slug')
        queryset = queryset.select_related('author')
        if self.request.GET.get('author'):
            author_submited_by_user = self.request.GET.get('author')
            if not author_submited_by_user == '':
                queryset = queryset.filter(author__username = author_submited_by_user)
        if self.request.GET.get('title'):
            title_submited_by_user = self.request.GET.get('title')
            if not title_submited_by_user == '':
                queryset = queryset.filter(title = title_submited_by_user)
        if self.request.GET.get('category'):
            category_choosed_by_user = self.request.GET.get('category')
            if not category_choosed_by_user == 'ALL':
                queryset = queryset.filter(category = category_choosed_by_user)
        return queryset




class ReadBookDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'book'
    model = Book
    pk_url_kwarg = 'pk_book'
    template_name = "read/book.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        chapters = book.chapters.all()
        context['chapters'] = chapters
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('author')
        return queryset


class ReadChapterDetailView(LoginRequiredMixin, PicturesAndTextAsElementsMixin, DetailView):
    context_object_name = 'chapter'
    model = Chapter
    pk_url_kwarg = 'pk_chapter'
    template_name = "read/chapter.html"
