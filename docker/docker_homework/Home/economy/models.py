from django.db import models

# Create your models here.
class EconomyNews(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(blank=True)
    paper = models.CharField(max_length=100)

    def __str__(self):
        return self.title
