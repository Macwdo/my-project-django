from django.db import models
# Create your models here.


choices = [
    ("Portuguese", "PT"),
    ("English", "EN"),
]


class Book(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=150)
    pages = models.SmallIntegerField(blank=True, null=True)
    price = models.SmallIntegerField()
    language = models.CharField(max_length=20, choices=choices)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
