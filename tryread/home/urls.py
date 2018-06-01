from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path(
        "",
        view=views.HomeTemplateView.as_view(),
        name="home"
    ),
    path(
        "landing/",
        view=views.LandingTemplateView.as_view(),
        name="landing"
    ),
    path(
        "landing/reader/",
        view=views.LandingReaderTemplateView.as_view(),
        name="landing-reader"
    ),
    path(
        "landing/writer/",
        view=views.LandingWriterTemplateView.as_view(),
        name="landing-writer"
    ),

]
