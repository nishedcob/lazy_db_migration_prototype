from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

    def __str__(self):
        return f"id={self.id} name={self.name} created={self.date_created} modified={self.date_modified}"

class UnrelatedThing(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

    def __str__(self):
        return f"id={self.id} name={self.name} created={self.date_created} modified={self.date_modified}"

class SubThing(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    thing = models.ForeignKey(Thing, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"id={self.id} name={self.name} created={self.date_created} modified={self.date_modified}"
