from django.forms import ModelForm
from .models import Book, Chapter, Picture, Text

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'subtitle',
            'description',
            'category',
            'tags',
        ]

class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = [
            'title',
            'nr',
        ]

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = [
            'picture',
            'nr',
        ]

class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = [
            'text',
            'nr',
        ]
