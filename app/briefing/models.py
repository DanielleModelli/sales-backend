from django.db import models

from django.db import models

class Retailer(models.Model):
    name = models.CharField(max_length=100)
    vendors = models.ManyToManyField('Vendor', related_name='retailers')

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Briefing(models.Model):
    name = models.CharField(max_length=100)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    responsible = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    release_date = models.DateField()
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
