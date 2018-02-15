from __future__ import unicode_literals
from django.db import models
# Create your models here.



# Create your models here.

class profile1(models.Model):
    name=models.CharField(max_length=128,blank=True)
    description=models.TextField(blank=True)
    def __unicode__(self):
        return self.name
