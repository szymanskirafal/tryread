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
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        #return reverse('book', kwargs={'pk': self.id})
        pass


class Chapter(TimeStampedModel):
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = 'chapters')
    nr = models.PositiveSmallIntegerField()
    published = models.BooleanField(default = False)
    slug_chapter = models.SlugField(max_length = 150)
    title = models.CharField(max_length = 150)
    
    class Meta:
        ordering = ['nr']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug_chapter = slugify(self.title)
        super(Chapter, self).save(*args, **kwargs)

    def get_absolute_url(self):
        #return reverse('book', kwargs={'pk': self.id})
        pass

#class Section(models.Model):
#    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE, related_name = 'texts')
#    text = models.TextField(max_length=20000)
#    picture = models.ImageField(upload_to="static/images/", blank = True)
#    nr = models.PositiveSmallIntegerField(default=1)

#    class Meta:
#        ordering = ['nr']

class Text(TimeStampedModel):
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE, related_name = 'texts')
    text = models.TextField(max_length=20000)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.text


class Picture(TimeStampedModel):
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE, related_name = 'pictures')
    picture = models.ImageField(upload_to="static/images/")

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.picture
