from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

class UnrelatedThing(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

class SubThing(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    thing = models.ForeignKey(Thing, null=True, on_delete=models.CASCADE)
