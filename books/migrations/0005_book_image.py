# Generated by Django 5.2 on 2025-04-24 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_borrow'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers/'),
        ),
    ]
