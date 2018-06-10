from django.forms import ModelForm
from .models import Book, Chapter, Text

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

class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = [
            'text',
        ]
