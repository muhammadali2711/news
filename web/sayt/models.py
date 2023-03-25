from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    content = models.CharField(max_length=56)
    slug = models.SlugField(max_length=56)
    is_menu = models.BooleanField(default=False)
    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)
            
        return super(Category, self).save(*args, **kwargs)



class News(models.Model):
    title = models.CharField(max_length=512)
    date = models.DateField(auto_now_add=True)
    short_description = models.TextField()
    description = models.TextField()
    img = models.ImageField()
    ctg = models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self):
        return self.title




