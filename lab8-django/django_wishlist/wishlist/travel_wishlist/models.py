from django.db import models

# Create your models here.
# models are classes that define structure of app's data and act as the interface to the db

class Place(models.Model):
    name = models.CharField(max_length=200)  # constraints
    visited = models.BooleanField(default=False)  # default values

    def __str__(self):
        return f'{self.name}, visited? {self.visited}'
