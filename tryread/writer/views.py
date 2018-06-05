from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, TemplateView

from books.forms import BookForm
from books.models import Book


class WriterAddBookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "writer/add-book.html"
    success_url = '/writer/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WriterBooksListView(LoginRequiredMixin, ListView):
    context_object_name = 'books'
    model = Book
    template_name = 'writer/books.html'

    def get_queryset(self):
        queryset = Book.objects.all().filter(author=self.request.user)
        return queryset


class WriterTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'writer/writer.html'
