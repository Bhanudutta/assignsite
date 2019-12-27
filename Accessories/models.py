from django.db import models

# Create your models here.
class ProductTree(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    parent_id = models.IntegerField(default=0)
