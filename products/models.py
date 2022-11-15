from django.db.models import Q
from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)

    def featured(self):
        return self.filter(featured = True, active = True)
    
    def search(self, query):
        lookups = (Q(title__contains = query) | 
                   Q(description__contains = query) | 
                   Q(price__contains = query))
        return self.filter(lookups).distinct()



class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using = self._db)
    
    def all(self):
        return self.get_queryset().active()

    def featured(self):
        #return self.get_queryset().filter(featured = True)
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    title = models.CharField('Títutlo', max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField('Description', max_length=None, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to = 'products/', null=True, blank=True)
    featured = models.BooleanField(default = False)
    active = models.BooleanField(default = True)


    objects = ProductManager()

    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug = self.slug)
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender = Product)