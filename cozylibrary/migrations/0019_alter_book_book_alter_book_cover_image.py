# Generated by Django 4.0.5 on 2022-08-03 08:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cozylibrary', '0018_remove_book_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='book_file'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='cover_image'),
        ),
    ]