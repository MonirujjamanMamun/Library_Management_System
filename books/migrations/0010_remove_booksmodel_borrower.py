# Generated by Django 4.2.7 on 2024-01-07 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_bookreview_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksmodel',
            name='borrower',
        ),
    ]