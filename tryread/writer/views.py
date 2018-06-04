from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from books.models import Book


class WriterTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'writer/writer.html'

class WriterAddBookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'subtitle', 'description', 'category', 'tags']
    template_name = "writer/add-book.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
