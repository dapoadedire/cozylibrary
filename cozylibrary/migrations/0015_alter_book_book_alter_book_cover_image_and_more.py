# Generated by Django 4.0.5 on 2022-07-31 14:54

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozylibrary', '0014_remove_book_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='cover_image'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('fantasy', 'Fantasy'), ('sci-fi', 'Sci-Fi'), ('romance', 'Romance'), ('mystery', 'Mystery'), ('biography', 'Biography'), ('thriller', 'Thriller'), ('drama', 'Drama'), ('horror', 'Horror'), ('history', 'History'), ('western', 'Western'), ('non-fiction', 'Non-Fiction'), ('poetry', 'Poetry'), ('children', 'Children'), ('self-help', 'Self-Help'), ('religion', 'Religion'), ('science', 'Science'), ('programming', 'Programming'), ('history', 'History'), ('other', 'Other'), ('fiction,', 'Fiction')], default='other', max_length=15),
        ),
    ]