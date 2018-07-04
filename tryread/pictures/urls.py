from django.urls import path

from . import views

app_name = "pictures"
urlpatterns = [
    path(
        'create/',
        view=views.PictureCreateView.as_view(),
        name='create'
    ),
    path(
        'detail/<int:pk>/',
        view=views.PictureDetailView.as_view(),
        name='detail'
    ),
    path(
        'update/<int:pk>/',
        view=views.PictureUpdateView.as_view(),
        name='update'
    ),

]
