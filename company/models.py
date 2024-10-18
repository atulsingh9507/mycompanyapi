from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    context = models.TextField()

    def __str__(self):
        return self.name
