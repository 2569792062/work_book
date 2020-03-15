from django.db import models



class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    times = models.DateTimeField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    brief = models.CharField(max_length=255, blank=True, null=True)
