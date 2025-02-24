from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

class Topic(models.Model):
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True,null=True)
    category    = models.ForeignKey(
        'Category',
        related_name="products",
        on_delete=models.CASCADE
    ) 

    def save(self, *args, **kwargs):
        if not self.slug:  # Prevent overwriting existing slugs
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)  # No need to specify the model name

    def get_absolute_url(self):
        return self.slug

class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"   

    def __str__(self):                           
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])
