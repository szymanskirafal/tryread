from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home:landing')
        else:
            return super(HomeTemplateView, self).get(request, *args, **kwargs)



class LandingTemplateView(TemplateView):
    template_name = 'home/landing.html'

class LandingReaderTemplateView(TemplateView):
    template_name = 'home/landing-reader.html'

class LandingWriterTemplateView(TemplateView):
    template_name = 'home/landing-writer.html'
