from django.db import models

class Movies (models.Model):
    name = models.CharField(max_length=100)
    yearReleased = models.IntegerField()
    rated = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name