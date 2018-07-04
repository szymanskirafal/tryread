from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from itertools import chain

from books.forms import BookForm, ChapterForm, PictureForm, TextForm
from books.models import Book, Chapter, Picture, Text

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

class WriterChapterUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'chapter'
    model = Chapter
    form_class = ChapterForm
    template_name = "writer/chapter-update.html"

    def get_success_url(self):
        pk = self.kwargs['pk']
        slug_chapter = self.kwargs['slug_chapter']
        slug = self.kwargs['slug']
        return reverse('writer:chapter', kwargs={'slug': slug, 'slug_chapter': slug_chapter, 'pk': pk})

class WriterChapterDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'chapter'
    model = Chapter
    template_name = 'writer/chapter.html'

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}

        if self.object:
            context['object'] = self.object
            pictures = Picture.objects.all().filter(chapter = self.object)
            texts = Text.objects.all().filter(chapter = self.object)
            list_of_elements = sorted(
                chain(pictures, texts),
                key=lambda element: element.created, reverse=False)
            context['elements'] = list_of_elements
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)

class WriterChapterPreviewDetailView(WriterChapterDetailView):
    template_name = 'writer/chapter-preview.html'


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

class WriterTextUpdateView(LoginRequiredMixin, UpdateView):
    model = Text
    form_class = TextForm
    template_name = "writer/text-update.html"

    def form_valid(self, form):

        print('-'*15, ' text update with element pk: ', self.object.pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('writer:chapter',
            kwargs={
                'slug': self.kwargs.get("slug_book"),
                'slug_chapter': self.kwargs.get("slug_chapter"),
                'pk': self.kwargs.get("pk_chapter"),
            }
        )



class WriterTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'writer/writer.html'

class WriterAddPictureCreateView(LoginRequiredMixin, CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'writer/add-picture.html'
    success_url = '/writer/'

    def form_valid(self, form):
        self.chapter = Chapter.objects.get(pk = self.kwargs.get('pk'))
        form.instance.chapter = self.chapter
        return super().form_valid(form)

class WriterPictureDeleteView(LoginRequiredMixin, DeleteView):
    model = Picture
    form_class = PictureForm
    pk_url_kwarg = 'pk_picture'
    success_url = '/writer/'
    template_name = 'writer/delete-picture.html'

    def get_success_url(self):
        return reverse('writer:chapter',
            kwargs={
                'slug': self.kwargs.get("slug_book"),
                'slug_chapter': self.kwargs.get("slug_chapter"),
                'pk': self.kwargs.get("pk_chapter"),
            }
        )

class WriterPictureUpdateView(LoginRequiredMixin, UpdateView):
    model = Picture
    form_class = PictureForm
    pk_url_kwarg = 'pk'
    success_url = '/writer/'
    template_name = 'writer/picture-update.html'

    def get_success_url(self):
        return reverse('writer:chapter',
            kwargs={
                'slug': self.kwargs.get("slug_book"),
                'slug_chapter': self.kwargs.get("slug_chapter"),
                'pk': self.kwargs.get("pk_chapter"),
            }
        )
