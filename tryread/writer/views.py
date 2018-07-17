from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from itertools import chain

from books.forms import BookForm, ChapterForm, ChapterPublishForm, PictureForm, TextForm
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
        from django.core.mail import send_mail

        send_mail(
            'Subject here',
            'Here is the message.',
            'postmaster@tryread.com',

            ['r.szymansky@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)


class WriterBookDetailView(LoginRequiredMixin, BooksWrittenByCurrentUserMixin, DetailView):
    context_object_name = 'book'
    model = Book
    pk_url_kwarg = 'pk_book'
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
        self.book = Book.objects.get(pk = self.kwargs.get('pk_book'))
        if self.book in Book.objects.all().filter(author=self.request.user):
            print('_'*15, ' to jest book napisana przez autora')

        form.instance.book = self.book
        return super().form_valid(form)

    def get_success_url(self):
        pk_book = self.kwargs.get('pk_book')
        slug_book = self.book.slug
        return reverse('writer:book', kwargs={'pk_book': pk_book, 'slug_book': slug_book})

class WriterChapterUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'chapter'
    form_class = ChapterForm
    model = Chapter
    pk_url_kwarg = 'pk_chapter'
    template_name = "writer/chapter-update.html"

    def get_success_url(self):
        pk_chapter = self.kwargs.get('pk_chapter')
        slug_chapter = self.kwargs.get('slug_chapter')
        slug_book = self.kwargs.get('slug')
        return reverse('writer:chapter',
            kwargs={
                'slug_book': slug_book,
                'slug_chapter': slug_chapter,
                'pk_chapter': pk_chapter
            }
        )

class PicturesAndTextAsElementsMixin():
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


class WriterChapterDetailView(LoginRequiredMixin, PicturesAndTextAsElementsMixin, DetailView):
    context_object_name = 'chapter'
    model = Chapter
    pk_url_kwarg = 'pk_chapter'
    template_name = 'writer/chapter.html'


class WriterChapterPreviewUpdateView(LoginRequiredMixin, PicturesAndTextAsElementsMixin, UpdateView):
    form_class = ChapterPublishForm
    model = Chapter
    pk_url_kwarg = 'pk_chapter'
    template_name = 'writer/chapter-preview.html'

    def form_valid(self, form):
        chapter = self.object
        if chapter.published:
            form.instance.published = False
        else:
            form.instance.published = True
        return super().form_valid(form)

    def get_success_url(self):
        pk_chapter = self.kwargs.get('pk_chapter')
        chapter = Chapter.objects.get(pk = pk_chapter)
        pk_book = chapter.book.pk
        return reverse('writer:book',
            kwargs={
                'slug_book': self.kwargs.get("slug_book"),
                'pk_book': pk_book,
            }
        )


class WriterTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'writer/writer.html'

class GetBackToChapterMixin():

    def get_success_url(self):
        return reverse('writer:chapter',
            kwargs={
                'slug_book': self.kwargs.get("slug_book"),
                'slug_chapter': self.kwargs.get("slug_chapter"),
                'pk_chapter': self.kwargs.get("pk_chapter"),
            }
        )

class WriterPictureCreateView(LoginRequiredMixin, GetBackToChapterMixin, CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'writer/picture-create.html'

    def form_valid(self, form):
        self.chapter = Chapter.objects.get(pk = self.kwargs.get('pk_chapter'))
        form.instance.chapter = self.chapter
        return super().form_valid(form)


class WriterPictureDeleteView(LoginRequiredMixin, GetBackToChapterMixin, DeleteView):
    context_object_name = 'picture'
    form_class = PictureForm
    model = Picture
    pk_url_kwarg = 'pk_picture'
    template_name = 'writer/picture-delete.html'


class WriterPictureUpdateView(LoginRequiredMixin, GetBackToChapterMixin, UpdateView):
    model = Picture
    form_class = PictureForm
    pk_url_kwarg = 'pk_picture'
    template_name = 'writer/picture-update.html'

class WriterTextCreateView(LoginRequiredMixin, GetBackToChapterMixin, CreateView):
    model = Text
    form_class = TextForm
    template_name = "writer/add-text.html"

    def form_valid(self, form):
        self.chapter = Chapter.objects.get(pk = self.kwargs.get('pk_chapter'))
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


class WriterTextDeleteView(LoginRequiredMixin, GetBackToChapterMixin, DeleteView):
    form_class = TextForm
    model = Text
    pk_url_kwarg = 'pk_text'
    template_name = "writer/text-delete.html"


class WriterTextUpdateView(LoginRequiredMixin, GetBackToChapterMixin, UpdateView):
    form_class = TextForm
    model = Text
    pk_url_kwarg = 'pk_text'
    template_name = "writer/text-update.html"
