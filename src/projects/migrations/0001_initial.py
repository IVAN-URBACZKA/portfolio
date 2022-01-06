# Generated by Django 4.0 on 2022-01-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Titre')),
                ('slug', models.SlugField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
