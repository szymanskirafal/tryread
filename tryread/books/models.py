from django.db import models

from tryread.users.models import User


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

    def get_absolute_url(self):
        #return reverse('book', kwargs={'pk': self.id})
        pass
