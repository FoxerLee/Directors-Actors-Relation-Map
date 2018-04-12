from django.db import models


# Create your models here.
class Relation1(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

