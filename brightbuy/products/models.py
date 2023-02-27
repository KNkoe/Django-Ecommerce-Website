from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class meta:
        ordering = ("name",)
        
    def __str__(self):
        return self.name