from django.db import models
from django.utils.text import slugify

from tryread.users.models import User

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Book(models.Model):
    ROMANCE = 'ROM'
    THRILLER = 'THR'
    MYSTERY = 'MYS'
    LIFE = 'LIF'
    DRAMA = 'DRA'
    HISTORIC = 'HIS'
    BIOGRAPHY = 'BIO'
    KIDS = 'KID'
    CATEGORIES = (
        (ROMANCE, 'Romance'),
        (THRILLER, 'Thriller'),
        (MYSTERY, 'Mystery'),
        (LIFE, 'Life'),
        (DRAMA, 'Drama'),
        (HISTORIC, 'Historic'),
        (BIOGRAPHY, 'Biography'),
        (KIDS, 'Kids'),)

    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'books_written')
    title = models.CharField(max_length = 150)
    subtitle = models.CharField(max_length = 300, blank = True)
    description = models.TextField(max_length = 3000, blank = True)
    slug = models.SlugField(max_length = 150)
    category = models.CharField(
        max_length=3,
        choices=CATEGORIES,
        default=ROMANCE,)
    tags = models.CharField(max_length = 250, blank = True)

    def __str__(self):
        return self.title + ' by ' + self.author.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book', kwargs={'pk': self.id})



class Chapter(TimeStampedModel):
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = 'chapters')
    nr = models.PositiveSmallIntegerField()
    published = models.BooleanField(default = False)
    slug = models.SlugField(max_length = 150)
    title = models.CharField(max_length = 150)

    class Meta:
        ordering = ['nr']

    def __str__(self):
        return self.title + ' from ' + self.book.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Chapter, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('chapter', kwargs={'pk_chapter': self.id})

    def next_chapter_pk(self):
        if Chapter.objects.filter(book=self.book, nr = self.nr+1).exists():
            next_chapter = Chapter.objects.filter(book=self.book, nr = self.nr+1).get()
            next_chapter_pk = next_chapter.pk
        else:
            next_chapter_pk = None
        return next_chapter_pk

    def previous_chapter_pk(self):
        if Chapter.objects.filter(book=self.book, nr = self.nr-1).exists():
            previous_chapter = Chapter.objects.filter(book=self.book, nr = self.nr-1).get()
            previous_chapter_pk = previous_chapter.pk
        else:
            previous_chapter_pk = None
        return previous_chapter_pk



class Text(TimeStampedModel):
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE, related_name = 'texts')
    text = models.TextField(max_length=20000)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.text


class Picture(TimeStampedModel):
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE, related_name = 'pictures')
    picture = models.ImageField(upload_to="images/")

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.picture
