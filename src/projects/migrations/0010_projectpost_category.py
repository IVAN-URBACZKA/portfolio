# Generated by Django 4.0 on 2022-01-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_categorypost'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpost',
            name='category',
            field=models.ManyToManyField(to='projects.CategoryPost'),
        ),
    ]
