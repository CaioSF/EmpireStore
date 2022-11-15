from django.db import models


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)

    def featured(self):
        return self.filter(featured = True, active = True)


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


class Product(models.Model):
    title = models.CharField('Títutlo', max_length=120)
    slug = models.SlugField(default = 'slug_padrao', unique = True)
    description = models.TextField('Description', max_length=None, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to = 'products/', null=True, blank=True)
    featured = models.BooleanField(default = False)
    active = models.BooleanField(default = True)


    objects = ProductManager()

    def __str__(self):
        return self.title