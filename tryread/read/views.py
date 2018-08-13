from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.views.generic.edit import FormMixin

from books.forms import BookFiltersForm
from books.models import Book, Chapter
from tryread.users.models import User


class ReadBooksListView(LoginRequiredMixin, FormMixin, ListView):
    context_object_name = 'books'
    form_class = BookFiltersForm
    model = Book
    template_name = "read/books.html"

    def get_queryset(self):
        queryset = Book.objects.all()
        author_submited_by_user = self.request.GET.get('author')
        title_submited_by_user = self.request.GET.get('title')
        category_choosed_by_user = self.request.GET.get('category')
        if not author_submited_by_user == '':
            queryset = queryset.filter(author__username = author_submited_by_user)
        if not title_submited_by_user == '':
            queryset = queryset.filter(title = title_submited_by_user)
        if not category_choosed_by_user == 'ALL':
            queryset = queryset.filter(category = category_choosed_by_user)
        return queryset




class ReadBookDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'book'
    model = Book
    pk_url_kwarg = 'pk_book'
    template_name = "read/book.html"

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}

        if self.object:
            context['object'] = self.object
            context['chapters'] = Chapter.objects.all().filter(book=self.object)
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)

class ReadChapterDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'chapter'
    model = Chapter
    pk_url_kwarg = 'pk_chapter'
    template_name = "read/chapter.html"
