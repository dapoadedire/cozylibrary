from django.db import models
from django.utils.timezone import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField

# Create your models here


class Book(models.Model):
    GENRE_CHOICES = (
        ("fantasy", "Fantasy"),
        ("sci-fi", "Sci-Fi"),
        ("romance", "Romance"),
        ("mystery", "Mystery"),
        ("biography", "Biography"),
        ("thriller", "Thriller"),
        ("drama", "Drama"),
        ("horror", "Horror"),
        ("history", "History"),
        ("western", "Western"),
        ("non-fiction", "Non-Fiction"),
        ("poetry", "Poetry"),
        ("children", "Children"),
        ("self-help", "Self-Help"),
        ("religion", "Religion"),
        ('science', "Science"),
        ('programming', "Programming"),
        ('history', "History"),
        ("other", "Other"),
        ('fiction,', "Fiction")
    )
    STATUS_CHOICES = (("draft", "Draft"), ("published", "Published"))
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    year = models.IntegerField(default=0)
    language = models.CharField(max_length=255, default="English")
    description = RichTextField(max_length=1000, blank=True)
    cover_image = CloudinaryField('cover_image',  blank=False, resource_type='image')
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    book =CloudinaryField('book_file',  blank=False, resource_type='raw')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
    slug = models.SlugField(max_length=50, unique=True, editable=False)

    def __str__(self):
        return f"{self.title } by  { self.author}"


    class Meta:
        ordering = ("-created_at",)

    def get_absolute_url(self):
        return reverse("book:detail", kwargs={"slug": self.slug})
