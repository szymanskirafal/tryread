from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView


class WriterTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'writer/writer.html'
