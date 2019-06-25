from django.db import models

# Create your models here.
class SmashTag(models.Model):
    tag = models.CharField(max_length=200)
    def __str__(self):
        return self.tag