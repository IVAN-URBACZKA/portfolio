# Generated by Django 4.0 on 2022-01-06 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_remove_projectpost_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoryPost',
        ),
    ]