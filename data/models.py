from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    last_accessed = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return f"id={self.id} name={self.name} created={self.date_created} modified={self.date_modified} last_accessed={self.last_accessed}"

class UnrelatedThing(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id={self.id} name={self.name} created={self.date_created} modified={self.date_modified}"

class SubThing(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    thing = models.ForeignKey(Thing, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"id={self.id} name={self.name} created={self.date_created} modified={self.date_modified} thing={self.thing_id}"
