from django.forms import ModelForm
from .models import Book, Chapter, Section

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

class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = [
            'text',
            'picture'
            'nr',
        ]
