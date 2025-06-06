# Generated by Django 4.2 on 2025-05-05 14:12

import cloudinary.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=isbn_field.fields.ISBNField(blank=True, max_length=28, null=True, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN'),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.PositiveSmallIntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2025)]),
        ),
        migrations.AddField(
            model_name='userslibroteka',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.role'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(default=1000),
        ),
    ]
