# Generated by Django 4.0 on 2022-01-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_projectpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpost',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]
