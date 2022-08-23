from inspect import classify_class_attrs
from django.db import models

# Create your models here.
class Comnents(models.Model):
    name = models.CharField(max_length=255,null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000,null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.name
