# Generated by Django 4.2.7 on 2024-01-06 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_booksmodel_user_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksmodel',
            name='user_reviews',
        ),
    ]