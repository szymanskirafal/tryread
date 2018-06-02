from django.urls import path

from . import views

app_name = "writer"
urlpatterns = [
    path(
        "",
        view=views.WriterTemplateView.as_view(),
        name="writer"
    ),

]
