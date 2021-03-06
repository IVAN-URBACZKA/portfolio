from django.db import models
from django.template.defaultfilters import slugify

class CategoryPost(models.Model):

    title = models.CharField(max_length=30, verbose_name="title cat")

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.title

class ProjectPost(models.Model):

    title = models.CharField(max_length=30, verbose_name="Titre")
    category = models.ManyToManyField(CategoryPost)
    content = models.TextField()
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='portfolio')


    class Meta:
        verbose_name = "Projet"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProjectPost, self).save(*args, **kwargs)