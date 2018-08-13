from django import forms
#from django.forms import ModelForm, HiddenInput
from .models import Book, Chapter, Picture, Text

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'subtitle',
            'description',
            'category',
            'tags',
        ]

class BookFiltersForm(forms.Form):
    ALL = 'ALL'
    ROMANCE = 'ROM'
    THRILLER = 'THR'
    MYSTERY = 'MYS'
    LIFE = 'LIF'
    DRAMA = 'DRA'
    HISTORIC = 'HIS'
    BIOGRAPHY = 'BIO'
    KIDS = 'KID'
    CATEGORIES = (
        (ALL, 'All'),
        (ROMANCE, 'Romance'),
        (THRILLER, 'Thriller'),
        (MYSTERY, 'Mystery'),
        (LIFE, 'Life'),
        (DRAMA, 'Drama'),
        (HISTORIC, 'Historic'),
        (BIOGRAPHY, 'Biography'),
        (KIDS, 'Kids'),)
    author = forms.CharField(max_length=150, required=False)
    title = forms.CharField(max_length=250, required=False)
    category = forms.ChoiceField(choices=CATEGORIES,)
    #tags = forms.CharField(max_length=250, required=False)


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = [
            'nr',
            'title',
        ]

class ChapterPublishForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = [
            'published',
        ]
        widgets = {'published': forms.HiddenInput()}

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = [
            'picture',
        ]

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = [
            'text',
        ]
