from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic

from .models import Picture


class PictureCreateView(generic.CreateView):

    fields = ["image"]
    model = Picture
    template_name = "pictures/create.html"
    success_url = '/'

class PictureDetailView(generic.DetailView):
    context_object_name = 'picture'
    model = Picture
    template_name = "pictures/detail.html"


class PictureUpdateView(generic.UpdateView):

    fields = ["image"]
    model = Picture
    pk_url_kwarg = 'pk'
    template_name = "pictures/update.html"
    success_url = '/'
