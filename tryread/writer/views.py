from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from books.forms import BookForm, ChapterForm
from books.models import Book, Chapter


class WriterAddBookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "writer/add-book.html"
    success_url = '/writer/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WriterAddChapterCreateView(LoginRequiredMixin, CreateView):
    model = Chapter
    form_class = ChapterForm
    template_name = "writer/add-chapter.html"
    success_url = '/writer/'

    def form_valid(self, form):
        book = Book.objects.get(slug = self.kwargs['slug'])
        form.instance.book = book
        return super().form_valid(form)



class BooksWrittenByCurrentUserMixin():
    def get_queryset(self):
        queryset = Book.objects.all().filter(author=self.request.user)
        return queryset

class WriterBookDetailView(LoginRequiredMixin, BooksWrittenByCurrentUserMixin, DetailView):
    context_object_name = 'book'
    model = Book
    template_name = 'writer/book.html'

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

class WriterBooksListView(LoginRequiredMixin, BooksWrittenByCurrentUserMixin, ListView):
    context_object_name = 'books'
    model = Book
    template_name = 'writer/books.html'

class WriterChapterDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'chapter'
    model = Chapter
    slug_field = "slug_chapter"
    slug_url_kwarg = "slug_chapter"
    template_name = 'writer/chapter.html'

    def get(self, request, *args, **kwargs):
        print('-'*10, 'self.args: ', self.args)
        print('*'*10)
        print('-'*10, 'self.kwargs: ', self.kwargs)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



class WriterTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'writer/writer.html'
