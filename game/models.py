from django.db import models


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)

    description = models.TextField(null=True)

    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = "game"
        ordering = ['title']

    def __str__(self):
        return self.title
