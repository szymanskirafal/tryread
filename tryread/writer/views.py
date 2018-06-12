from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from books.forms import BookForm, ChapterForm, TextForm
from books.models import Book, Chapter, Text

class BooksWrittenByCurrentUserMixin():
    def get_queryset(self):
        queryset = Book.objects.all().filter(author=self.request.user)
        return queryset

class WriterBookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "writer/add-book.html"
    success_url = '/writer/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


class WriterChapterCreateView(LoginRequiredMixin, CreateView):
    model = Chapter
    form_class = ChapterForm
    template_name = "writer/add-chapter.html"

    def form_valid(self, form):
        self.book = Book.objects.get(pk = self.kwargs.get('pk'))
        form.instance.book = self.book
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('writer:book', kwargs={'pk': pk, 'slug':self.book.slug})


class WriterChapterDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'chapter'
    model = Chapter
    template_name = 'writer/chapter.html'

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}

        if self.object:
            context['object'] = self.object
            context['texts'] = Text.objects.all().filter(chapter = self.object)
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)

class WriterSectionDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'section'
    model = Text
    template_name = 'writer/section-detail.html'

class WriterSectionUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'section'
    form_class = TextForm
    model = Text
    template_name = 'writer/section-update.html'

class WriterSectionDeleteView(LoginRequiredMixin, DeleteView):
    context_object_name = 'section'
    model = Text
    template_name = 'writer/section-delete.html'

    def get_success_url(self):
        print("-"*15, 'slug: ', self.object.chapter.book.slug)
        print("-"*15, 'slug from kwargs: ', self.kwargs.get('slug'))

        return reverse_lazy('writer:books')
        # kwargs={'slug': self.kwargs.get('slug'), 'slug_chapter':self.kwargs.get('slug_chapter'), 'pk_chapter':self.kwargs.get('pk_chapter')})


class WriterTextCreateView(LoginRequiredMixin, CreateView):
    model = Text
    form_class = TextForm
    template_name = "writer/add-text.html"

    def form_valid(self, form):
        self.chapter = Chapter.objects.get(pk = self.kwargs.get('pk'))
        form.instance.chapter = self.chapter
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}

        if self.object:
            context['object'] = self.object
            context['chapter'] = self.chapter
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse('writer:chapter',
            kwargs={
                'slug': self.chapter.book.slug,
                'slug_chapter': self.chapter.slug_chapter,
                'pk': self.chapter.pk,
            }
        )



class WriterTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'writer/writer.html'
