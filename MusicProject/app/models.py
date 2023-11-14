from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Musician(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    founding_date = models.DateField()
    description = models.TextField()
    slug = models.SlugField(max_length=255,
                            blank=True,
                            unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(f"{self.name}")
        return super().save()

    def __str__(self):
        return f"{self.name} - {self.genre} - {self.founding_date} - {self.description}"


class MusicGenre(models.Model):
    genre_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.genre_name}"

    # def get_absolute_url(self):
        # return reverse( 'queen_page.html', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255,
                            blank=True,
                            unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(f"{self.name} - {self.price}")
        return super().save()

    def __str__(self):
        return f"{self.name} - {self.price}"
